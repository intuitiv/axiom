# Axiom: A Framework for Reliable AI Applications

Axiom is a new paradigm for prompt engineering that transforms the "dark art" of writing prompts into a structured, testable, and maintainable engineering discipline. It's built for developers and teams who want to build robust, predictable, and reliable applications powered by Large Language Models.

With Axiom, you stop treating prompts as simple strings and start treating them as **source code**.

---

### The Axiom Philosophy

The core of the Axiom framework is the `.axiom` file—a declarative, self-contained artifact that defines the entire behavior of an AI feature. This approach is built on three pillars:

1.  **Test-Driven Prompting:** Define the "correct" behavior of your AI with a powerful assertion-based testing suite. Write your tests first, then use the Axiom workflow to engineer a prompt that passes them.

2.  **AI-Assisted Improvement:** When a test fails, Axiom doesn't just report it. The `improve` command uses a meta-LLM as your co-pilot to analyze the failure and suggest targeted, logical changes to your prompt's rules, automating the most tedious part of prompt engineering.

3.  **Intelligent Compilation:** Axiom's SDK acts as a "transpiler," converting your high-level `.axiom` file into a state-of-the-art, optimized system prompt. It automatically handles best practices like JSON enforcement, few-shot example formatting, and rule injection, so you don't have to.

### Features

*   **Declarative Language:** A clean, readable syntax (`.axiom` files) for defining persona, rules, data schemas, and tests.
*   **Assertion-Based Testing:** Write powerful tests for your prompts, including deterministic checks and **semantic assertions** (`~=`) that use an AI validator to check for intent and meaning.
*   **AI-Powered `improve` Workflow:** Automatically find failing tests and get intelligent, AI-generated suggestions to fix your prompt's logic.
*   **Automatic Few-Shot Example Generation:** "Promote" your passing tests into high-quality, validated few-shot examples with the `compile-examples` command.
*   **Professional Tooling:** A full command-line interface (CLI) and `Makefile` for a seamless development workflow.

### Getting Started

#### Prerequisites

*   Python 3.10+
*   An ANTLR4 build tool (e.g., `brew install antlr` or download the JAR)
*   A locally running LLM server (like LM Studio or Ollama) accessible at `http://localhost:1234`

#### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:intuitiv/axiom.git
    cd axiom_project
    ```

2.  **Set up a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    *(You will need to create a `requirements.txt` file)*
    ```bash
    pip install antlr4-python3-runtime click jinja2 openai dpath
    ```

4.  **Build the Parser:**
    This is a one-time step (and is run automatically by other commands). It generates the Python parser from the `Axiom.g4` grammar.
    ```bash
    make build
    ```

### The Axiom Workflow

The development cycle is simple, powerful, and iterative.

1.  **Write a Test:** Open an `.axiom` file (e.g., `examples/sentiment_analyzer.axiom`) and define your goal in the `assert` block.

2.  **Run the Test:** See the baseline performance. Expect failures!
    ```bash
    make test FILE=examples/sentiment_analyzer.axiom
    ```

3.  **Improve the Prompt:** Use the AI co-pilot to fix the first failing test.
    ```bash
    make improve FILE=examples/sentiment_analyzer.axiom
    ```
    The AI will suggest new rules. Review and approve them, and the SDK will update your file.

4.  **Re-Test:** Run `make test` again to confirm the fix. Repeat the `improve` -> `test` loop until all tests pass.

5.  **Compile Examples:** Once all tests pass, lock in the high-quality outputs as few-shot examples.
    ```bash
    make compile FILE=examples/sentiment_analyzer.axiom
    ```

Your `.axiom` file is now a production-ready artifact, containing logic, tests, and validated examples.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
