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

# Phony targets are commands that don't represent actual files.
.PHONY: all build clean rebuild run test compile