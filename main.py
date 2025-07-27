import logging
import json
from axiom.sdk import AxiomSDK
from jinja2 import Template
import click

from llm.llm_interface import LLMInterface

# --- Setup ---
# Set up basic logging to show INFO and above.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def _initialize_sdk():
    """Helper to initialize the SDK and handle connection errors."""
    try:
        llm = LLMInterface()
        sdk = AxiomSDK(llm_interface=llm)
        return sdk
    except Exception as e:
        logging.error(f"Failed to initialize SDK. Is your LLM server running? Error: {e}")
        # click.echo is a better way to print in CLI apps
        click.secho(f"ERROR: Failed to initialize SDK. Is your LLM server running?", fg='red')
        raise click.Abort()  # Exit the CLI gracefully


def _parse_inputs(inputs: tuple) -> dict:
    """Parses a tuple of 'key=value' strings into a dictionary."""
    data = {}
    for item in inputs:
        key, value = item.split('=', 1)
        # Try to parse the value as JSON (for structs/objects)
        try:
            data[key] = json.loads(value)
        except json.JSONDecodeError:
            # If it fails, treat it as a plain string
            data[key] = value
    return data


# --- CLI Definition ---

@click.group()
@click.option('--verbose', '-v', is_flag=True, help="Enable verbose logging from the LLM interface.")
def cli(verbose):
    """
    Axiom: A framework for building reliable AI applications.
    This CLI provides tools to test, improve, and compile .axiom prompt files.
    """
    # Configure logging level based on the verbose flag
    log_level = logging.INFO if verbose else logging.ERROR
    logging.basicConfig(level=log_level, format='%(levelname)s: (%(name)s) %(message)s')

    # Suppress verbose logs from the lmstudio library unless --verbose is used
    if not verbose:
        lmstudio_logger = logging.getLogger("lmstudio")
        lmstudio_logger.setLevel(logging.WARNING)


@cli.command()
@click.argument('filepath', type=click.Path(exists=True))
def test(filepath: str):
    """
    Run all assertion-based tests in an axiom file.

    This command executes the prompt for each test with an 'asserts' block
    and validates the LLM's output against the defined assertions.
    """
    sdk = _initialize_sdk()
    sdk.test(filepath)


@cli.command('compile-examples')
@click.argument('filepath', type=click.Path(exists=True))
def compile_examples(filepath: str):
    """
    Run tests and update the 'expected_output' block for passing tests.

    This command runs all assertion tests. For each test that PASSES, it
    "promotes" the successful LLM output to be a canonical few-shot example
    by inserting or updating the 'expected_output' block in the .axiom file.
    """
    sdk = _initialize_sdk()
    sdk.compile_examples(filepath)

@cli.command()
@click.argument('filepath', type=click.Path(exists=True, dir_okay=False))
@click.option('--test-name', '-t', default=None, help="The name of the failing test to improve.")
def improve(filepath: str, test_name: str):
    """Suggest new rules to fix a failing test."""
    sdk = _initialize_sdk()
    sdk.improve(filepath, test_name)


@cli.command()
@click.argument('filepath', type=click.Path(exists=True))
@click.option('--input', '-i', 'inputs', multiple=True,
              help="Input data in 'key=value' format. For objects, use 'key=\"{\"json\":\"object\"}\"'.")
def generate(filepath: str, inputs: tuple):
    """
    Generate the System and User prompts without executing them.

    This is a debugging tool to see the final prompts that would be sent
    to the LLM. It loads the axiom file, transpiles it (including any compiled
    examples), and renders the final user payload with the provided inputs.
    """
    sdk = _initialize_sdk()

    print(f"\n--- Generating Prompts for: {filepath} ---")
    system_prompt, user_payload_template = sdk.load(filepath)

    print("\n" + "=" * 70)
    click.secho("✅ COMPONENT 1: THE SYSTEM PROMPT", fg='green', bold=True)
    print("=" * 70)
    print(system_prompt)

    if inputs:
        user_data = _parse_inputs(inputs)
        final_user_message = Template(user_payload_template).render(**user_data)

        print("\n" + "=" * 70)
        click.secho("✅ COMPONENT 2: THE FINAL USER PROMPT", fg='green', bold=True)
        print("=" * 70)
        print(final_user_message)
    else:
        print("\n" + "=" * 70)
        click.secho("✅ COMPONENT 2: USER PAYLOAD TEMPLATE (no inputs provided)", fg='yellow', bold=True)
        print("=" * 70)
        print(user_payload_template)

    print("\n")


@cli.command()
@click.argument('filepath', type=click.Path(exists=True, dir_okay=False))
def validate(filepath: str):
    """Analyzes prompt rules and tests for logical conflicts."""
    sdk = _initialize_sdk()
    sdk.validate(filepath)

if __name__ == "__main__":
    cli()