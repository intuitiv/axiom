# llm_interface.py
import logging
import os
import json
import re

from openai import OpenAI
import lmstudio as lms
logger = logging.getLogger(__name__)

class LLMInterface:
    def __init__(self):
        # Point to the local server
        self.client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
        lms.configure_default_client("localhost:1234")
        try:
            self.model = lms.llm("google/gemma-3n-e4b")
            logger.info(f"LMStudioLLMInterface initialized. Pointing to: localhost:1234")
            self.is_reachable = False  # Flag for initial health check
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client for LM Studio: {e}")
            raise Exception("Could not initialize LM Studio client.") from e

    def execute(self, system_prompt: str, user_prompt: str) -> dict:
        """
        Executes a prompt against the LLM and returns the parsed JSON output.
        """
        logger.debug("\n--- Sending to LLM ---")
        response_str = None
        try:
            chat = lms.Chat(system_prompt)
            chat.add_user_message(user_prompt)
            response_message = self.model.respond(chat, config={
                "temperature": 0.1,
                # "maxTokens": 50,
            })
            response_str = response_message.content
            logger.debug("--- LLM Response ---")
            clean_json = self.clean_json_string(response_str.strip()).strip()
            try:
                # The content should already be a valid JSON string
                json_data = json.loads(clean_json)
                logger.debug(f"LM STUDIO: Successfully extracted structured JSON data. \n {json_data}")
                return json_data
            except json.JSONDecodeError as e:
                try:
                    return self.fix_and_load_json(clean_json)
                except e:
                    logger.error(
                        f"LLM returned invalid JSON despite JSON mode request: {response_str}")
                    raise e
        except json.JSONDecodeError as e:
            logger.error(f"ERROR: Could not decode JSON from LLM response: {e}")
            return {"error": "Invalid JSON response", "details": response_str}
        except Exception as e:
            logger.error(f"ERROR: An unexpected error occurred while calling the LLM: {e}")
            return {"error": "LLM API call failed", "details": str(e)}

    def fix_and_load_json(self, json_str: str) -> dict | None:
        lines = json_str.splitlines()
        fixed_lines = []
        stack = []

        for line in lines:
            stripped = line.strip()

            # Opening brackets
            if stripped.endswith('{') or stripped.endswith('['):
                stack.append(stripped[-1])
                fixed_lines.append(line)
                continue

            # Closing brackets
            if stripped.endswith(']') or stripped.endswith('}'):
                if stack:
                    expected = stack[-1]
                    actual = stripped[-1]

                    if expected == '{' and actual == ']':
                        # Wrong close: should be }
                        line = line.rstrip()[:-1] + '}'
                        stack.pop()
                    elif expected == '[' and actual == '}':
                        # Wrong close: should be ]
                        line = line.rstrip()[:-1] + ']'
                        stack.pop()
                    elif expected == actual:
                        stack.pop()
                fixed_lines.append(line)
            else:
                fixed_lines.append(line)

        # Final check: if top-level closing bracket is mismatched
        if fixed_lines:
            last = fixed_lines[-1].strip()
            if last == ']':
                fixed_lines[-1] = '}'
            elif last == '}':
                if stack and stack[-1] == '[':
                    fixed_lines[-1] = ']'

        fixed_json = "\n".join(fixed_lines)

        try:
            return json.loads(fixed_json)
        except json.JSONDecodeError as e:
            logger.error("❌ Still broken:", e)
            logger.error("---- Fixed Output ----")
            logger.error(fixed_json)
            raise e

    def clean_json_string(self, s):
        # Remove markdown-style triple backtick code fences
        match = re.search(r"```json\s*(.*?)\s*```", s, re.DOTALL)
        if match:
            logger.debug("Got text in json markdown format")
            json_str = match.group(1)
            return json_str.strip()
        return s