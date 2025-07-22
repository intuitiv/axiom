from jinja2 import Template

from axiom.sdk import AxiomSDK


def main():
    """Demonstrates how to use the AxiomSDK."""
    print("Initializing Axiom SDK...")
    sdk = AxiomSDK()

    try:
        # 1. Load the axiom file.
        filepath = "email_drafter.axiom"
        print(f"\nLoading and transpiling '{filepath}'...")
        system_prompt, user_payload_template = sdk.load(filepath)

        print("✅ Transpilation successful!")

        # 2. Prepare the real user data for this specific run.
        real_user_data = {
            "user_name": "Casey",
            "plan_name": "Enterprise",
            "service_name": "DataWeave"
        }

        # 3. Render the final user message.
        final_user_message = Template(user_payload_template).render(**real_user_data)

        # 4. Display the results.
        print_results(system_prompt, final_user_message)

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


def print_results(system_prompt, user_message):
    """Helper function to print the generated components."""
    print("\n" + "=" * 70)
    print("✅ COMPONENT 1: THE SYSTEM PROMPT (Ready for API)")
    print("=" * 70)
    print(system_prompt)

    print("\n" + "=" * 70)
    print("✅ COMPONENT 2: THE FINAL USER PROMPT (Ready for API)")
    print("=" * 70)
    print(user_message)
    print("\n")


if __name__ == "__main__":
    main()