# Makefile for the Axiom Project
# Automates ANTLR parser generation, testing, and example compilation.

# --- Variables ---
GRAMMAR_FILE := axiom/parser/Axiom.g4
OUTPUT_DIR := ./gen
GENERATED_FILES := $(OUTPUT_DIR)/AxiomLexer.py \
                   $(OUTPUT_DIR)/AxiomParser.py \
                   $(OUTPUT_DIR)/AxiomVisitor.py
PYTHON_RUN = .venv/bin/python # Or your python interpreter
AXIOM_FILE = sentiment_analyzer.axiom
# The default .axiom file to use if none is specified.
FILE ?= sentiment_analyzer.axiom
# The default test name for 'improve-specific'. Leave empty for automatic mode.
NAME ?=

# --- Main Workflow Commands ---

# Default command: build the parser, run tests, then compile examples.
# This is the standard workflow for making a change.
all: build test compile

# A command to just run a demo of the prompt.
run: build
	@echo "🚀 Running Axiom Prompt (Demo)..."
	$(PYTHON_RUN) main.py run $(AXIOM_FILE)

# Run all assertion-based tests for the specified FILE.
test: build
	@echo "--- Running Assertion Tests for [$(FILE)] ---"
	$(PYTHON_RUN) main.py test $(FILE)

# Automatically find and improve the first failing test in FILE.
improve: build
	@echo "--- Improving Failed Test in [$(FILE)] (Automatic Mode) ---"
	$(PYTHON_RUN) main.py improve $(FILE)

# Improve a SPECIFIC failing test in FILE.
# Usage: make improve-test FILE=your.axiom TEST_NAME="The Test Name"
improve-test: build
	@echo "--- Improving Specific Test in [$(FILE)] ---"
	@if [ -z "$(NAME)" ]; then \
		echo "ERROR: NAME variable is not set."; \
		echo "Usage: make improve-specific NAME=\"Your Test Name\""; \
		exit 1; \
	fi
	$(PYTHON_RUN) main.py improve $(FILE) --test-name "$(NAME)"

# Compile all passing tests in FILE into 'expected_output' examples.
compile: build
	@echo "--- Compiling Passing Tests to Examples for [$(FILE)] ---"
	$(PYTHON_RUN) main.py compile-examples $(FILE)

# Generate and print the final system prompt for FILE.
generate: build
	@echo "--- Generating Final System Prompt for [$(FILE)] ---"
	$(PYTHON_RUN) main.py generate $(FILE)
# --- Build Automation ---

# Build the parser only if the grammar has changed.
# This is now the prerequisite for all other commands.
build: $(GENERATED_FILES)
	@echo "✅ ANTLR parser is up-to-date."

# The core ANTLR generation rule.
$(GENERATED_FILES): $(GRAMMAR_FILE)
	@echo "ℹ️  Grammar file changed. Regenerating ANTLR parser..."
	@antlr4 -Dlanguage=Python3 $(GRAMMAR_FILE) -o $(OUTPUT_DIR) -visitor -no-listener

# A command to force a rebuild.
rebuild: clean build

# A command to clean up all generated files.
clean:
	@echo "🧹 Cleaning up generated ANTLR and Python cache files..."
	@rm -f $(OUTPUT_DIR)/AxiomLexer.py \
		  $(OUTPUT_DIR)/AxiomParser.py \
		  $(OUTPUT_DIR)/AxiomVisitor.py \
		  $(OUTPUT_DIR)/Axiom.tokens \
		  $(OUTPUT_DIR)/AxiomLexer.interp \
		  $(OUTPUT_DIR)/AxiomParser.interp
	@find . -type d -name "__pycache__" -exec rm -r {} +

completion-script:
	@echo '# Axiom Makefile Completion Script'
	@echo '_axiom_make_completion() {'
	@echo '    local cur_word prev_word; cur_word="$${COMP_WORDS[COMP_CWORD]}"; prev_word="$${COMP_WORDS[COMP_CWORD-1]}"'
	@echo '    if [[ "$$prev_word" == "FILE=" ]]; then'
	@echo '        COMPREPLY=( $$(compgen -G "*.axiom" -- "$$cur_word") )'
	@echo '        return 0'
	@echo '    fi'
	@echo '    if [[ "$$prev_word" == "TEST_NAME=" ]]; then'
	@echo '        local axiom_file; for word in "$${COMP_WORDS[@]}"; do if [[ "$$word" == FILE=* ]]; then axiom_file="$${word#*=}"; break; fi; done'
	@echo '        if [[ -n "$$axiom_file" && -f "$$axiom_file" ]]; then'
	@echo '            local test_names=$$(grep -oP ''test\\s*\"\\K[^\"]+'' "$$axiom_file")'
	@echo '            COMPREPLY=( $$(compgen -W "$${test_names}" -- "$$cur_word") )'
	@echo '        fi'
	@echo '        return 0'
	@echo '    fi'
	@echo '}'
	@echo 'compdef _axiom_make_completion make'


# Phony targets are commands that don't represent actual files.
.PHONY: all build clean rebuild run test compile completion-script improve improve-test generate

help:
	@echo ""
	@$(PYTHON_RUN) -c "import click; \
		click.secho('Axiom Prompt Engineering Framework', bold=True); \
		print(''); \
		click.secho('Usage:', bold=True); \
		print('  make <command> [OPTIONS]'); \
		print(''); \
		click.secho('Recommended Setup:', bold=True, fg='yellow'); \
		print('  For a better experience, add this alias to your ~/.bashrc or ~/.zshrc file:'); \
		click.secho('    alias axiom-setup=\'eval \"$$(make completion-script)\"\'', fg='cyan'); \
		print('  Then, run `axiom-setup` once per terminal session to enable smart Tab completion.'); \
		print(''); \
		click.secho('Options:', bold=True); \
		print('  FILE=<filename>         Specify the .axiom file to use (default: sentiment_analyzer.axiom)'); \
		print('  TEST_NAME=<test_name>   Specify the test name for ''improve-specific'''); \
		print(''); \
		click.secho('Workflow Commands:', bold=True); \
		print('  make test               Run all assertion-based tests for the specified FILE.'); \
		print('  make improve              Automatically find and fix the first failing test in FILE.'); \
		print('  make improve-test   Fix a specific failing test in FILE (requires TEST_NAME).'); \
		print('  make compile            Compile all passing tests in FILE into few-shot examples.'); \
		print('  make generate           Print the final, compiled system prompt for FILE.'); \
		print('');"