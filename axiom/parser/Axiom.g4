grammar Axiom;

// Parser Rules (start with lowercase)
prompt: block* EOF;

block: meta_block | persona_block | rules_block | interface_block | config_block | payload_block | tests_block;

meta_block: 'meta' '{' meta_field* '}';
meta_field: KEY ':' STRING;

persona_block: 'persona' ':' STRING;

rules_block: 'rules' '{' rule_item* '}';
rule_item: '-' STRING;

interface_block: 'interface' '{' interface_body* '}';
interface_body: types_block | inputs_block | outputs_block;

types_block: 'types' '{' struct_def* '}';
struct_def: 'struct' KEY '{' field_def* '}';

inputs_block: 'inputs' '{' field_def* '}';
outputs_block: 'outputs' '{' field_def* '}';

// CORRECTED: The literal 'description' is removed to avoid ambiguity with the KEY token.
// The visitor will now be responsible for identifying the description key.
field_def: KEY ':' type_def directive_block? (KEY ':' STRING)?;

directive_block: '(' (directive_pair (',' directive_pair)*)? ')';
directive_pair: KEY ':' value;

type_def: primitive_type | KEY | enum_def | list_def;
primitive_type: 'String' | 'Float' | 'Int' | 'Boolean';
enum_def: 'Enum' '(' (STRING (',' STRING)*)? ')';
list_def: 'List' '<' type_def '>';

config_block: 'config' '{' config_field* '}';
config_field: KEY ':' value;

payload_block: 'payload' MULTILINE_CONTENT;
tests_block: 'tests' '{' test_case* '}';
test_case: 'test' STRING '{' test_field* '}';
test_field: inputs_test_block | expected_output_block;

inputs_test_block: 'inputs' '{' inputs_test_pair* '}';
inputs_test_pair: KEY ':' STRING;

expected_output_block: 'expected_output' MULTILINE_CONTENT;

value: STRING | 'true' | 'false' | SIGNED_NUMBER;

// Lexer Rules (start with uppercase)
KEY: [a-zA-Z_] [a-zA-Z0-9_]*;
STRING: '"' (~["\\] | '\\' .)*? '"';
SIGNED_NUMBER: '-'? [0-9]+ ('.' [0-9]+)?;
MULTILINE_CONTENT: '<<<' .*? '>>>';

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' .*? '\n' -> skip;