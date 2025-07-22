# Makefile for the Axiom Project
# Automates ANTLR parser generation.

# --- Variables ---
# Define the location of the grammar file relative to this Makefile
GRAMMAR_FILE := axiom/parser/Axiom.g4

# Define the output directory for generated files
OUTPUT_DIR := axiom/parser

# List of files that ANTLR will generate
GENERATED_FILES := $(OUTPUT_DIR)/AxiomLexer.py \
                   $(OUTPUT_DIR)/AxiomParser.py \
                   $(OUTPUT_DIR)/AxiomVisitor.py

# --- Commands ---

# Default command to run when you just type 'make'
all: build

# The 'build' command. It depends on the generated files.
# This means 'make' will check if the generated files need to be created or updated.
build: $(GENERATED_FILES)
	@echo "✅ ANTLR parser is up-to-date."

# This is the core rule. It tells Make that the generated files
# DEPEND ON the grammar file. This command will only run if
# Axiom.g4 has been modified more recently than any of the generated files.
$(GENERATED_FILES): $(GRAMMAR_FILE)
	@echo "ℹ️  Grammar file changed. Regenerating ANTLR parser..."
	antlr4 -Dlanguage=Python3 $(GRAMMAR_FILE) -o $(OUTPUT_DIR) -visitor -no-listener

# A command to force a rebuild even if files are up-to-date
rebuild: clean build

# A command to clean up generated ANTLR files
clean:
	@echo "🧹 Cleaning up generated ANTLR files..."
	@rm -f $(OUTPUT_DIR)/AxiomLexer.py \
		  $(OUTPUT_DIR)/AxiomParser.py \
		  $(OUTPUT_DIR)/AxiomVisitor.py \
		  $(OUTPUT_DIR)/Axiom.tokens \
		  $(OUTPUT_DIR)/AxiomLexer.interp \
		  $(OUTPUT_DIR)/AxiomParser.interp

# Phony targets are commands that don't represent actual files.
.PHONY: all build clean rebuild
