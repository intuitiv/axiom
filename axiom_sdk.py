import json
from pathlib import Path
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from jinja2 import Template

# Import generated files
from AxiomLexer import AxiomLexer
from AxiomParser import AxiomParser
from axiom_visitor import AxiomVisitorImpl # Our custom visitor

class AxiomSDK:
    def _parse_and_transform(self, filepath: str) -> dict:
        input_stream = FileStream(filepath, encoding='utf-8')
        lexer = AxiomLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AxiomParser(stream)
        tree = parser.prompt()

        visitor = AxiomVisitorImpl()
        return visitor.visit(tree)

    def _generate_system_prompt(self, prompt_dict: dict) -> str:
        # This logic remains the same as it consumes the final dictionary
        persona = f"# PERSONA\n{prompt_dict.get('persona', 'You are a helpful AI assistant.')}"
        rules = ""
        if 'rules' in prompt_dict:
            rule_items = "\n".join([f"- {r}" for r in prompt_dict['rules']])
            rules = f"# CORE INSTRUCTIONS & LOGIC\nYou must follow these rules when generating your response:\n{rule_items}"
        output_parts = ["# OUTPUT FORMAT", "Your final response MUST be a single, valid JSON object. Do not include any other text or explanations. The JSON object must have the following keys and adhere to these field-specific constraints:"]
        if 'outputs' in prompt_dict.get('interface', {}):
            for field in prompt_dict['interface']['outputs']:
                field_str = f"\n- \"{field['name']}\":\n  - Type: {field['type']}"
                if 'directives' in field:
                    for key, val in field['directives'].items():
                        field_str += f"\n  - {key.replace('_', ' ').title()}: {val}"
                output_parts.append(field_str)
        output_format = "\n".join(output_parts)
        examples_block = ""
        config = prompt_dict.get('config', {})
        if config.get('use_tests_as_examples', False) and 'tests' in prompt_dict:
            payload_template = Template(prompt_dict.get("payload", ""))
            example_parts = []
            for test in prompt_dict['tests']:
                user_msg = payload_template.render(**test['inputs']).strip()
                asst_msg = json.dumps(test['expected_output'])
                example_parts.append(f"User:\n{user_msg}\n\nAssistant:\n{asst_msg}")
            examples_str = "\n\n".join(example_parts)
            examples_block = f"--- EXAMPLES START ---\n\n{examples_str}\n\n--- EXAMPLES END ---"
        system_prompt_header = "You are a helpful assistant. Below are a few examples of how to respond to various user inputs. After the examples, respond only to the final user input."
        full_prompt = "\n\n".join(filter(None, [system_prompt_header, persona, rules, output_format, examples_block]))
        return full_prompt.strip()

    def load(self, filepath: str) -> tuple[str, str]:
        prompt_dict = self._parse_and_transform(filepath)
        system_prompt = self._generate_system_prompt(prompt_dict)
        user_payload_template = prompt_dict.get("payload", "")
        return system_prompt, user_payload_template