#compdef make

# Axiom Framework Completion for Zsh
# To activate in your current session, run: source axiom-completion.zsh

_axiom_get_test_names() {
    # This helper function finds the FILE= argument on the command line
    # and extracts the test names from that file.
    local file_arg
    # The '(I)' flag finds the index of the first match
    file_arg=${words[(I)FILE=*]}

    if [[ -n "$file_arg" ]]; then
        # Remove the "FILE=" prefix to get the path
        file_arg=${file_arg#*=}
        if [[ -f "$file_arg" ]]; then
            # Grep the test names and add them as completion suggestions
            _values 'test name' ${(f)"$(grep -oP 'test\s*\"\K[^\"]+' $file_arg)"}
        fi
    fi
}

# This is the main completion function, now using the robust _arguments helper.
_axiom_completion() {
    _arguments \
        'FILE=:[Axiom File to process]:_files -g "*.axiom"' \
        'TEST_NAME=:[Test Name to improve]:_axiom_get_test_names' \
        '*:make command:((build\:Regenerate\ the\ ANTLR\ parser \
                          test\:Run\ all\ assertion-based\ tests \
                          improve\:Automatically\ improve\ the\ first\ failing\ test \
                          improve-specific\:Improve\ a\ specific\ failing\ test \
                          compile\:Compile\ passing\ tests\ into\ examples \
                          generate\:Generate\ the\ final\ system\ prompt \
                          clean\:Remove\ generated\ ANTLR\ files \
                          help\:Show\ this\ help\ message))'
}

# Register the function to handle completions for the 'make' command.
_axiom_completion "$@"