import json
import re
import textwrap
import difflib
import click
from pathlib import Path
from antlr4 import FileStream, CommonTokenStream
from jinja2 import Template

from gen.axiom.parser.AxiomLexer import AxiomLexer
from gen.axiom.parser.AxiomParser import AxiomParser
from llm.llm_interface import LLMInterface
# Relative imports for the package structure
from .assertions import assertion_helpers
from .parser.visitor import AxiomVisitorImpl


class AxiomSDK:
    """
    The main SDK for loading, parsing, testing, improving, and compiling .axiom files.
    """

    def __init__(self, llm_interface):
        self.llm = llm_interface
        try:
            grammar_path = Path(__file__).parent / "parser" / "Axiom.g4"
            if not grammar_path.exists():
                raise FileNotFoundError
        except FileNotFoundError:
            raise RuntimeError("Could not find 'Axiom.g4' in axiom/parser directory. Did you run the build script?")

        # Initialize parser components
        self._lexer = AxiomLexer(None)
        self._parser = AxiomParser(None)
        self._visitor = AxiomVisitorImpl()

    # --- Core Private Methods ---

    def _parse_and_transform(self, filepath: Path, visited_files=None) -> dict:
        """
        Recursively parses an axiom file and its imports, with cycle detection.
        """
        if visited_files is None:
            visited_files = set()
        str_filepath = str(filepath.resolve())
        if str_filepath in visited_files:
            return {}
        visited_files.add(str_filepath)

        input_stream = FileStream(str_filepath, encoding='utf-8')
        self._lexer.inputStream = input_stream
        stream = CommonTokenStream(self._lexer)
        self._parser.setInputStream(stream)
        tree = self._parser.prompt()
        prompt_dict = self._visitor.visit(tree)

        if "imports" in prompt_dict and prompt_dict["imports"]:
            merged_imports = {}
            for imp in prompt_dict["imports"]:
                import_path = filepath.parent / imp['path']
                imported_dict = self._parse_and_transform(import_path, visited_files)
                for part in imp['parts']:
                    if part in imported_dict:
                        if part not in merged_imports:
                            merged_imports[part] = {} if isinstance(imported_dict[part], dict) else []
                        if isinstance(imported_dict[part], dict):
                            self._deep_merge_dicts(merged_imports.setdefault(part, {}), imported_dict[part])
                        elif isinstance(imported_dict[part], list):
                            merged_imports.setdefault(part, []).extend(imported_dict[part])
            prompt_dict = self._deep_merge_dicts(merged_imports, prompt_dict)

        return prompt_dict

    def _deep_merge_dicts(self, base, new):
        """Helper to recursively merge dictionaries and extend lists."""
        for key, value in new.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._deep_merge_dicts(base[key], value)
            elif isinstance(value, list) and key in base and isinstance(base[key], list):
                for item in value:
                    if item not in base[key]:
                        base[key].append(item)
            else:
                base[key] = value
        return base

    def _generate_system_prompt(self, prompt_dict: dict, use_examples=True) -> str:
        """The core transpiler logic that builds the master system prompt."""
        persona = f"# PERSONA\n{prompt_dict.get('persona', 'You are a helpful AI assistant.')}"

        rules_list = prompt_dict.get('rules', [])
        rules = ""
        if rules_list:
            rule_texts = [r['text'] for r in self._normalize_rules(rules_list) if r['status'] != 'deleted']
            rule_items = "\n".join([f"- {text}" for text in rule_texts])
            rules = f"# CORE INSTRUCTIONS & LOGIC\nYou must follow these rules:\n{rule_items}"

        output_parts = ["# OUTPUT FORMAT", "Your response MUST be a single, valid JSON object with the following keys:"]
        if 'outputs' in prompt_dict.get('interface', {}):
            for field in prompt_dict['interface']['outputs']:
                field_str = f"\n- \"{field['name']}\" ({field['type']})"
                if 'directives' in field:
                    for key, val in field['directives'].items():
                        field_str += f", {key.replace('_', ' ')}: {val}"
                output_parts.append(field_str)
        output_format = "\n".join(output_parts)

        examples_block = ""
        config = prompt_dict.get('config', {})
        if use_examples and config.get('use_tests_as_examples', False) and 'tests' in prompt_dict:
            payload_template = Template(prompt_dict.get("payload", ""))
            example_parts = [t for t in prompt_dict['tests'] if 'expected_output' in t]
            if example_parts:
                examples_str = "\n\n".join(
                    f"User:\n{payload_template.render(**t['inputs']).strip()}\n\nAssistant:\n{json.dumps(t['expected_output'], indent=2)}"
                    for t in example_parts
                )
                examples_block = f"--- EXAMPLES START ---\n\n{examples_str}\n\n--- EXAMPLES END ---"

        system_prompt_header = "You are an assistant that follows instructions precisely. After the examples, respond only to the final user input."
        full_prompt = "\n\n".join(filter(None, [system_prompt_header, persona, rules, output_format, examples_block]))
        return full_prompt.strip()

    @classmethod
    def log_semantic(cls, sm_check):
        return ' ~= ' + '"' + sm_check + '"' if sm_check else ''

    def _run_single_test(self, test_case: dict, system_prompt: str, user_payload_template: Template):
        """
        A helper to run one test, now with the correct logic for handling
        both standard and semantic assertions.
        """
        test_name = test_case['name']
        click.secho(f"\n[RUNNING] Test: \"{test_name}\"", fg='cyan')
        user_prompt = user_payload_template.render(**test_case['inputs'])

        llm_output = self.llm.execute(system_prompt, user_prompt)
        click.echo("  - LLM Output Received:")
        click.echo(textwrap.indent(json.dumps(llm_output, indent=2), '    '))

        if "error" in llm_output:
            click.secho(f"  - ❌ FAIL (LLM call failed)", fg='red')
            return test_name, False, "LLM call failed", llm_output

        click.echo("  - Evaluating Assertions:")
        for assertion in test_case.get('assert', []):
            expression = assertion['expression']
            semantic_check = assertion.get('semantic_check')

            full_assertion_str = f"{expression} {AxiomSDK.log_semantic(semantic_check)}"
            click.echo(f"    - Checking: {full_assertion_str}")

            try:
                # Always prepare the context for evaluation
                context = {"output": llm_output, **assertion_helpers}

                if not semantic_check:
                    # --- Standard Assertion Path ---
                    # The expression itself is the entire boolean check.
                    result = eval(expression, {"__builtins__": {}}, context)
                    if not result:
                        click.secho(f"    - ❌ FAILED", fg='red')
                        return test_name, False, expression, llm_output
                    else:
                        click.secho(f"    - ✅ PASSED", fg='green')
                else:
                    # --- Semantic Assertion Path ---
                    # The expression is just the LEFT side, to get the content.
                    content_to_check = eval(expression, {"__builtins__": {}}, context)

                    validator_prompt = self._construct_semantic_check_prompt(content_to_check, semantic_check)
                    validation_response = self.llm.execute(validator_prompt, "Validate.")

                    if validation_response.get("isValid") is True:
                        click.secho(f"    - ✅ SEMANTIC CHECK PASSED", fg='green')
                    else:
                        click.secho(f"    - ❌ SEMANTIC CHECK FAILED", fg='red')
                        return test_name, False, full_assertion_str, llm_output

            except Exception as e:
                click.secho(f"    - ❌ ERROR during evaluation: {e}", fg='red')
                return test_name, False, f"Error evaluating: {expression}", llm_output

        click.secho(f"\n  - ✅ All assertions PASSED for \"{test_name}\"", fg='green', bold=True)
        return test_name, True, None, llm_output

    def _serialize_to_axiom_string(self, prompt_dict: dict) -> str:
        """Takes a prompt dictionary and writes it back to a formatted .axiom string."""
        content = []

        def escape(s: str) -> str:
            return s.replace('"', '\\"')

        def format_kv_pair(key, value, indent=4):
            val_str = ""
            if isinstance(value, str):
                val_str = f'"{escape(value)}"'
            elif isinstance(value, bool):
                val_str = str(value).lower()
            elif isinstance(value, (int, float)):
                val_str = str(value)
            elif isinstance(value, dict):
                val_str = json.dumps(value)
            return f"{' ' * indent}{key}: {val_str}"

        def format_field(field, indent=8):
            parts = [f"{' ' * indent}{field['name']}: {field['type']}"]
            if "directives" in field and field["directives"]:
                dir_items = []
                for k, v in field["directives"].items():
                    val_str = json.dumps(v)
                    dir_items.append(f'{k}: {val_str}')
                parts.append(f"({', '.join(dir_items)})")
            return " ".join(parts)

        if "imports" in prompt_dict and prompt_dict["imports"]:
            for imp in prompt_dict["imports"]:
                parts = ", ".join(imp['parts'])
                content.append(f"import {{ {parts} }} from \"{imp['path']}\"\n")

        if "meta" in prompt_dict:
            content.append("meta {")
            content.extend([format_kv_pair(k, v) for k, v in prompt_dict["meta"].items()])
            content.append("}\n")

        if "persona" in prompt_dict:
            content.append(f'persona: "{escape(prompt_dict["persona"])}"\n')

        if "rules" in prompt_dict and prompt_dict["rules"]:
            content.append("rules {")
            for rule in self._normalize_rules(prompt_dict["rules"]):
                text, status = rule.get('text', ''), rule.get('status', 'original')
                line = f'    - "{escape(text)}"'
                if status == 'added':
                    line += " // added by AI"
                elif status == 'updated':
                    line += " // updated by AI"
                elif status == 'deleted':
                    line = f'    // - "{escape(text)}" // deleted by AI'
                content.append(line)
            content.append("}\n")

        if "types" in prompt_dict:
            content.append("types {")
            for name, fields in prompt_dict["types"].items():
                content.append(f"    struct {name} {{")
                content.extend([format_field(f) for f in fields])
                content.append("    }")
            content.append("}\n")

        if "interface" in prompt_dict:
            content.append("interface {")
            if "inputs" in prompt_dict["interface"]:
                content.append("    inputs {")
                content.extend([format_field(f) for f in prompt_dict["interface"]["inputs"]])
                content.append("    }")
            if "outputs" in prompt_dict["interface"]:
                content.append("    outputs {")
                content.extend([format_field(f) for f in prompt_dict["interface"]["outputs"]])
                content.append("    }")
            content.append("}\n")

        if "config" in prompt_dict:
            content.append("config {")
            content.extend([format_kv_pair(k, v) for k, v in prompt_dict["config"].items()])
            content.append("}\n")

        if "payload" in prompt_dict:
            payload_content = textwrap.indent(prompt_dict["payload"].strip(), '    ')
            content.append(f"payload <<<\n{payload_content}\n>>>\n")

        if "tests" in prompt_dict:
            content.append("tests {")
            for test in prompt_dict["tests"]:
                content.append(f'    test "{escape(test["name"])}" {{')
                if "inputs" in test:
                    content.append("        inputs {")
                    content.extend([format_kv_pair(k, v, indent=12) for k, v in test["inputs"].items()])
                    content.append("        }")
                if "assert" in test:
                    content.append("        assert {")
                    content.extend([f'            - "{escape(a)}"' for a in test["assert"]])
                    content.append("        }")
                if "expected_output" in test:
                    output_json = json.dumps(test["expected_output"], indent=4)
                    indented_json = textwrap.indent(output_json, '            ')
                    content.append(f"        expected_output <<<\n{indented_json}\n        >>>")
                content.append("    }")
            content.append("}\n")

        return "\n".join(content)

    def _normalize_rules(self, rules: list) -> list:
        """Ensures all rules are in the structured dict format for processing."""
        normalized = []
        for rule in rules:
            if isinstance(rule, str):
                normalized.append({'text': rule, 'status': 'original'})
            elif isinstance(rule, dict):
                # Ensure status exists, default to original
                rule.setdefault('status', 'original')
                normalized.append(rule)
        return normalized

    def _construct_semantic_check_prompt(self, content_to_check: any, requirement: str) -> str:
        return f"""You are a precise and strict validation AI. Your task is to determine if a given piece of content satisfies a specific requirement.
**Content to Analyze:**
{json.dumps(content_to_check, indent=2)}
**Requirement to Check:**
"{requirement}"
**YOUR TASK:**
Does the 'Content to Analyze' satisfy the 'Requirement to Check'? Respond with a single, valid JSON object with one key, "isValid", which is a boolean.
"""

    def _construct_brainstorm_meta_prompt(self, p_dict, test, bad_output, failed_assertion):
        """Constructs the NEW "brainstorm" prompt for the meta-LLM."""
        persona = p_dict.get('persona', 'A helpful AI assistant.')
        rules = [r['text'] for r in self._normalize_rules(p_dict.get('rules', [])) if r['status'] != 'deleted']

        return f"""You are an expert prompt engineering co-pilot. Your task is to brainstorm multiple, distinct strategies to fix a failing prompt.

**Analysis of the Failure**
1.  **Input:** {json.dumps(test['inputs'])}
2.  **The AI Produced This Incorrect Output:** {json.dumps(bad_output)}
3.  **This Specific Assertion Failed:** `{failed_assertion}`

**Existing Ruleset:**
{json.dumps(rules, indent=2)}

**YOUR TASK:**
Propose exactly three distinct, creative strategies to fix the logical failure. For each strategy, provide a brief "reason" explaining your approach and a complete "proposed_rules" list.

**Strategies to Consider:**
- **Strategy 1 (Modify):** Modify an existing vague rule to be more precise.
- **Strategy 2 (Add Specific):** Add a new, highly specific rule to handle this edge case.
- **Strategy 3 (Add General):** Add a new, more general principle that guides the AI's reasoning.

**CRITICAL INSTRUCTIONS:**
- **BE DIVERSE:** The three strategies must be meaningfully different from each other.
- **BE MINIMAL:** Do not suggest unnecessary changes.
- **DO NOT** simply restate the failed assertion as a rule.

Your response must be a single, valid JSON object with one key, "strategies", which is a list of three strategy objects.

**JSON Schema for your response:**
{{
  "strategies": [
    {{
      "reason": "<Brief explanation of Strategy 1>",
      "proposed_rules": ["<Complete list of rules for Strategy 1>"]
    }},
    {{
      "reason": "<Brief explanation of Strategy 2>",
      "proposed_rules": ["<Complete list of rules for Strategy 2>"]
    }},
    {{
      "reason": "<Brief explanation of Strategy 3>",
      "proposed_rules": ["<Complete list of rules for Strategy 3>"]
    }}
  ]
}}
"""

    def _construct_test_conflict_meta_prompt(self, test1: dict, test2: dict) -> str:
        return f"""You are a logical analyst. Your task is to determine if two test cases for an AI prompt are contradictory.
A contradiction exists if the inputs are highly similar, but the required outputs (defined by assertions) are logically incompatible.

**Test Case 1: "{test1['name']}"**
- Inputs: {json.dumps(test1['inputs'])}
- Assertions: {json.dumps(test1.get('assert', []))}

**Test Case 2: "{test2['name']}"**
- Inputs: {json.dumps(test2['inputs'])}
- Assertions: {json.dumps(test2.get('assert', []))}

**YOUR TASK:**
Respond with a single JSON object.
- If they are contradictory, respond with: `{{"is_conflicting": true, "reason": "<brief explanation>"}}`
- If they are NOT contradictory, respond with: `{{"is_conflicting": false}}`"""

    def _construct_improve_meta_prompt(self, p_dict, test, bad_output, failed_assertion, previous_failures=None):
        """Constructs the NEW, self-correcting Chain-of-Thought prompt for the meta-LLM."""
        persona = p_dict.get('persona', 'A helpful AI assistant.')
        rules = [r['text'] for r in self._normalize_rules(p_dict.get('rules', [])) if r['status'] != 'deleted']

        feedback_block = ""
        if previous_failures:
            feedback_items = "\n".join(f"- {failure}" for failure in previous_failures)
            feedback_block = f"""
**CRITICAL FEEDBACK ON PREVIOUS ATTEMPTS:**
You have failed before. Read this feedback carefully and DO NOT repeat these same mistakes.
{feedback_items}
"""

        return f"""You are an expert prompt engineering logician. Your task is to fix a failing prompt by suggesting a minimal, targeted change to its rules.

**Analysis of the Failure**
1.  **Input:** {json.dumps(test['inputs'])}
2.  **The AI Produced This Incorrect Output:** {json.dumps(bad_output)}
3.  **This Specific Assertion Failed:** `{failed_assertion}`

**Existing Ruleset to Modify:**
{json.dumps(rules, indent=2)}
{feedback_block}
**YOUR TASK:**
First, think step-by-step to arrive at a solution. Then, provide the final proposed ruleset in a valid JSON object.

**Chain of Thought Steps:**
1.  **Failure Analysis:** Why did the output `{json.dumps(bad_output)}` fail the assertion `{failed_assertion}`? Be specific.
2.  **Root Cause Diagnosis:** Based on the persona and existing rules, why did the AI produce this output? Is a rule too vague? Is a specific case not handled?
3.  **Correction Strategy:** What is the most minimal, logical change that can be made to the rules to fix this? This might be modifying a rule, adding a new one, or deleting a bad one.
4.  **Synthesize Final Ruleset:** Based on your strategy, construct the new, complete list of rules. Preserve all valid original rules.

**CRITICAL INSTRUCTIONS:**
- **DO NOT** simply restate the failed assertion as a rule (e.g., if assertion is `x > 0.8`, do not add the rule "x must be > 0.8"). Instead, deduce a more general principle (e.g., "Confidence for mixed reviews should be high.").
- **AVOID REDUNDANCY.** Do not suggest a rule that is semantically identical to an existing one.
- **DO NOT** add rules about the JSON output format; that is handled automatically.

Your final response must be a single JSON object with two keys: "thought" (containing your chain of thought) and "proposed_rules" (containing the complete, final list of rules).
"""

    def _construct_validation_meta_prompt(self, rules: list, check_type: str) -> str:
        """Constructs the NEW, more robust meta-prompt for validation."""
        if check_type == "conflict":
            task_description = "Analyze for logical contradictions. A conflict occurs when two rules cannot both be true simultaneously (e.g., 'be concise' vs 'be verbose')."
            json_schema = '{"is_conflicting": boolean, "conflicts": [ { "rule1": "<...>", "rule2": "<...>", "reason": "<...>" } ]}'
        else:  # redundancy
            task_description = "Analyze for semantic redundancy. Redundancy occurs when two rules convey the same instruction (e.g., 'output JSON' vs 'the response must be JSON')."
            json_schema = '{"is_redundant": boolean, "redundancies": [ { "rules": ["<...>", "<...>"], "reason": "<...>" } ]}'

        return f"""You are a meticulous logical analyst. Your task is to analyze a list of instructions for an AI and identify specific logical flaws.

**TASK:**
{task_description}

**RULES TO ANALYZE:**
{json.dumps(rules, indent=2)}

**RESPONSE FORMAT:**
Your response MUST be a single, valid JSON object that conforms to the schema. If no flaws are found, the main boolean key must be false and the list must be empty.
**JSON Schema:**
{json_schema}
"""

    def _validate_rules(self, rules: list) -> tuple[bool, dict | None]:
        """Validates a list of rules and now returns detailed failure reasons."""
        if len(rules) < 2: return True, None

        conflict_meta_prompt = self._construct_validation_meta_prompt(rules, "conflict")
        conflict_response = self.llm.execute(conflict_meta_prompt, "Analyze.")
        if "error" in conflict_response: return True, {"type": "warning",
                                                       "message": "Meta-LLM call for conflict check failed."}
        if conflict_response.get("is_conflicting"):
            return False, {"type": "conflict", "details": conflict_response.get("conflicts", [])}

        redundancy_meta_prompt = self._construct_validation_meta_prompt(rules, "redundancy")
        redundancy_response = self.llm.execute(redundancy_meta_prompt, "Analyze.")
        if "error" in redundancy_response: return True, {"type": "warning",
                                                         "message": "Meta-LLM call for redundancy check failed."}
        if redundancy_response.get("is_redundant"):
            return False, {"type": "redundancy", "details": redundancy_response.get("redundancies", [])}

        return True, None

    def _run_all_tests_and_get_failures(self, prompt_dict: dict) -> list:
        """Runs all assertion tests and returns a list of failure details."""
        system_prompt = self._generate_system_prompt(prompt_dict, use_examples=False)
        user_payload_template = Template(prompt_dict.get("payload", ""))
        failing_tests = []
        tests_to_run = [t for t in prompt_dict.get('tests', []) if 'assert' in t]

        for test in tests_to_run:
            name, passed, failed_assertion, output = self._run_single_test(test, system_prompt, user_payload_template)
            if not passed:
                failing_tests.append({
                    "name": name,
                    "failed_assertion": failed_assertion,
                    "output": output,
                    "inputs": test['inputs'],
                    "asserts": test['assert']
                })
        return failing_tests

    # --- Public API Methods ---

    def load(self, filepath: str) -> tuple[str, str]:
        prompt_dict = self._parse_and_transform(Path(filepath))
        system_prompt = self._generate_system_prompt(prompt_dict)
        return system_prompt, prompt_dict.get("payload", "")

    def test(self, filepath: str) -> bool:
        prompt_dict = self._parse_and_transform(Path(filepath))
        system_prompt = self._generate_system_prompt(prompt_dict, use_examples=False)
        user_payload_template = Template(prompt_dict.get("payload", ""))
        all_passed = True
        tests_to_run = [t for t in prompt_dict.get('tests', []) if 'assert' in t]
        if not tests_to_run:
            print("No assertion tests found.")
            return True
        for test in tests_to_run:
            _, passed, _, _ = self._run_single_test(test, system_prompt, user_payload_template)
            if not passed: all_passed = False
        print("\n--- Test Summary ---")
        if all_passed:
            print("✅ All assertion tests passed!")
        else:
            print("❌ Some assertion tests failed.")
        return all_passed

    def compile_examples(self, filepath: str):
        print(f"\n--- Compiling Examples for: {filepath} ---")
        path_obj = Path(filepath)
        prompt_dict = self._parse_and_transform(path_obj)
        system_prompt = self._generate_system_prompt(prompt_dict, use_examples=False)
        user_payload_template = Template(prompt_dict.get("payload", ""))
        file_was_modified = False
        for test_case_dict in prompt_dict.get('tests', []):
            if 'assert' not in test_case_dict: continue
            _, passed, _, llm_output = self._run_single_test(test_case_dict, system_prompt, user_payload_template)
            if passed:
                print(f"  - ✅ Assertions PASSED. Promoting to example for \"{test_case_dict['name']}\".")
                test_case_dict['expected_output'] = llm_output
                file_was_modified = True
            else:
                print(f"  - ❌ Assertions FAILED. Skipping promotion for \"{test_case_dict['name']}\".")
        if file_was_modified:
            print(f"\n✅ Writing updated examples to {filepath}")
            new_content = self._serialize_to_axiom_string(prompt_dict)
            path_obj.write_text(new_content, encoding="utf-8")
        else:
            print("\nNo changes made to the file.")

    # --- DEFINITIVE FIX: Rewritten Validation Logic ---

    def _validate_test_cases(self, prompt_dict: dict) -> bool:
        """Validates the test suite for contradictory assertions."""
        tests = [t for t in prompt_dict.get('tests', []) if 'assert' in t]
        if len(tests) < 2:
            print("  - ✅ No test conflicts found (fewer than 2 assertion tests).")
            return True

        for i in range(len(tests)):
            for j in range(i + 1, len(tests)):
                test1, test2 = tests[i], tests[j]
                meta_prompt = self._construct_test_conflict_meta_prompt(test1, test2)
                response = self.llm.execute(meta_prompt, "Analyze.")
                if response.get("is_conflicting"):
                    click.secho(f"  - ❌ Test Conflict Found between \"{test1['name']}\" and \"{test2['name']}\"",
                                fg='red')
                    click.echo(f"    Reason: {response.get('reason')}")
                    return False

        print("  - ✅ No test conflicts found.")
        return True

    def improve(self, filepath: str, test_name: str = None):
        """
        Intelligently improves a prompt. If a test_name is provided, it focuses
        on that test. Otherwise, it finds the first failing test and improves it.
        """
        path_obj = Path(filepath)
        print(f"\n--- Improving Prompt for: {filepath} ---")
        prompt_dict = self._parse_and_transform(path_obj)
        user_payload_template = Template(prompt_dict.get("payload", ""))

        failing_test_details = None

        if test_name:
            # --- User has specified a test to focus on ---
            print(f"\n[Step 1/3] Focusing on specified test: \"{test_name}\"")
            target_test = next((t for t in prompt_dict.get('tests', []) if t['name'] == test_name and 'assert' in t),
                               None)
            if not target_test:
                click.secho(f"❌ ERROR: Test named '{test_name}' with an 'assert' block not found.", fg='red')
                return

            system_prompt = self._generate_system_prompt(prompt_dict, use_examples=False)
            _, passed, failed_assertion, bad_output = self._run_single_test(target_test, system_prompt,
                                                                            user_payload_template)

            if passed:
                click.secho("\n✅ Specified test is already passing. Nothing to improve.", fg='green')
                return

            failing_test_details = {
                "name": test_name,
                "failed_assertion": failed_assertion,
                "output": bad_output,
                "inputs": target_test['inputs'],
                "asserts": target_test['assert']
            }
        else:
            # --- No test specified, automatically find the first failure ---
            print("\n[Step 1/3] No specific test provided. Finding first failure...")
            failures = self._run_all_tests_and_get_failures(prompt_dict)
            if not failures:
                click.secho("\n✅ All tests passed! Nothing to improve.", fg='green')
                return

            failing_test_details = failures[0]
            click.secho(
                f"\nAutomatically selected the first failing test to improve: \"{failing_test_details['name']}\"",
                fg='yellow')

        # --- At this point, we have a definite failing test in `failing_test_details` ---

        print("\n[Step 2/3] Brainstorming solutions with AI co-pilot...")
        meta_prompt = self._construct_brainstorm_meta_prompt(
            prompt_dict,
            failing_test_details,  # Pass the whole details dictionary
            failing_test_details['output'],
            failing_test_details['failed_assertion']
        )
        suggestion_response = self.llm.execute(meta_prompt, "Provide your suggestions.")

        if "error" in suggestion_response or "strategies" not in suggestion_response:
            click.secho("❌ Meta-LLM failed to generate valid strategies. Please try again.", fg='red')
            return

        strategies = suggestion_response['strategies']

        while True:
            print("\n--- AI Co-pilot suggests the following strategies: ---")
            for i, strategy in enumerate(strategies):
                click.secho(f"[{i + 1}] Strategy: {strategy['reason']}", bold=True)
                original_rule_texts = [r['text'] for r in self._normalize_rules(prompt_dict.get('rules', [])) if
                                       r.get('status') != 'deleted']
                matcher = difflib.SequenceMatcher(None, original_rule_texts, strategy['proposed_rules'])
                for tag, i1, i2, j1, j2 in matcher.get_opcodes():
                    if tag == 'delete' or tag == 'replace':
                        for text in original_rule_texts[i1:i2]: click.secho(f"    - {text}", fg='red')
                    if tag == 'insert' or tag == 'replace':
                        for text in strategy['proposed_rules'][j1:j2]: click.secho(f"    + {text}", fg='green')

            try:
                choice = int(input("\nChoose a strategy to sandbox test (1, 2, 3) or 0 to exit: "))
                if choice == 0:
                    print("Exiting.")
                    return
                chosen_strategy = strategies[choice - 1]
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")
                continue

            print(f"\n[Step 3/3] Sandbox testing Strategy #{choice}...")
            temp_prompt_dict = prompt_dict.copy()
            temp_prompt_dict['rules'] = chosen_strategy['proposed_rules']
            temp_system_prompt = self._generate_system_prompt(temp_prompt_dict, use_examples=False)

            # The test to run is the one we identified at the start
            test_to_rerun = next((t for t in prompt_dict.get('tests', []) if t['name'] == failing_test_details['name']),
                                 None)
            _, test_passed, _, _ = self._run_single_test(test_to_rerun, temp_system_prompt, user_payload_template)

            if test_passed:
                click.secho("\n✅ This strategy worked! The test now passes.", fg='green', bold=True)
                if input("Apply these changes to the file? (y/n): ").lower() == 'y':
                    prompt_dict['rules'] = chosen_strategy['proposed_rules']
                    new_content = self._serialize_to_axiom_string(prompt_dict)
                    path_obj.write_text(new_content, encoding="utf-8")
                    print(f"✅ Successfully updated rules in {filepath}")
                else:
                    print("Changes discarded.")
                return
            else:
                click.secho("\n❌ This strategy did not work. The test still fails.", fg='red', bold=True)
                if input("Try another strategy? (y/n): ").lower() != 'y':
                    print("Exiting.")
                    return

    def validate(self, filepath: str) -> bool:
        """
        Analyzes prompt rules and tests for contradictions and redundancies.
        """
        print(f"\n--- Validating Logic for: {filepath} ---")
        prompt_dict = self._parse_and_transform(Path(filepath))

        # 1. Validate rules
        print("\n[Checking rules for issues...]")
        rules = [r['text'] for r in self._normalize_rules(prompt_dict.get('rules', [])) if r['status'] != 'deleted']
        rules_are_valid, details = self._validate_rules(rules)

        if rules_are_valid and details and details.get('type') == 'warning':
            print(f"  - ⚠️  {details['message']}")
        elif not rules_are_valid:
            if details.get('type') == 'conflict':
                for conflict in details['details']:
                    click.secho(
                        f"  - ❌ CONFLICT: \"{conflict.get('rule1')}\" contradicts \"{conflict.get('rule2')}\"",
                        fg='red')
                    click.echo(f"      Reason: {conflict.get('reason')}")
            elif details.get('type') == 'redundancy':
                for redundancy in details['details']:
                    rules_str = '", "'.join(redundancy.get('rules', []))
                    click.secho(f"  - ❌ REDUNDANCY: The rules \"{rules_str}\" are semantically similar.",
                                fg='yellow')
                    click.echo(f"      Reason: {redundancy.get('reason')}")
        else:
            print("  - ✅ No contradictions or redundancies found in rules.")

        # 2. Validate tests
        print("\n[Checking tests for contradictions...]")
        tests_are_valid = self._validate_test_cases(prompt_dict)

        is_valid = rules_are_valid and tests_are_valid
        print("\n--- Validation Summary ---")
        if is_valid:
            click.secho("✅ Logic and tests are valid!", fg='green')
        else:
            click.secho("❌ Logic or tests have issues. Please review.", fg='red')
        return is_valid