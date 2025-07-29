import json

from gen.axiom.parser.AxiomParser import AxiomParser
from gen.axiom.parser.AxiomVisitor import AxiomVisitor


class AxiomVisitorImpl(AxiomVisitor):
    def visitPrompt(self, ctx: AxiomParser.PromptContext):
        result = {"imports": [self.visit(imp) for imp in ctx.import_statement()]}
        for block_ctx in ctx.block():
            result.update(self.visit(block_ctx))
        return result

    def visitImport_statement(self, ctx: AxiomParser.Import_statementContext):
        path = ctx.STRING().getText()[1:-1]
        parts = [key.getText() for key in ctx.import_key()]
        return {"path": path, "parts": parts}

    def visitImport_key(self, ctx: AxiomParser.Import_keyContext):
        return ctx.getText()

    def visitMeta_block(self, ctx: AxiomParser.Meta_blockContext):
        return {"meta": dict([self.visit(mf) for mf in ctx.meta_field()])}

    def visitPersona_block(self, ctx: AxiomParser.Persona_blockContext):
        return {"persona": ctx.STRING().getText()[1:-1]}

    def visitRules_block(self, ctx: AxiomParser.Rules_blockContext):
        return {"rules": [item.getText()[1:-1] for item in ctx.rule_item()]}

    def visitRule_item(self, ctx: AxiomParser.Rule_itemContext):
        return ctx.STRING().getText()

    def visitInterface_block(self, ctx: AxiomParser.Interface_blockContext):
        d = {}
        for body in ctx.interface_body(): d.update(self.visit(body))
        return {"interface": d}

    def visitConfig_block(self, ctx: AxiomParser.Config_blockContext):
        return {"config": dict([self.visit(cf) for cf in ctx.config_field()])}

    def visitPayload_block(self, ctx: AxiomParser.Payload_blockContext):
        return {"payload": ctx.MULTILINE_CONTENT().getText()[3:-3].strip()}

    def visitTests_block(self, ctx: AxiomParser.Tests_blockContext):
        return {"tests": [self.visit(tc) for tc in ctx.test_case()]}

    def visitTypes_block(self, ctx: AxiomParser.Types_blockContext):
        return {"types": dict([self.visit(s) for s in ctx.struct_def()])}

    def visitStruct_def(self, ctx: AxiomParser.Struct_defContext):
        key = ctx.ID().getText()
        fields = [self.visit(f) for f in ctx.field_def()]
        return key, fields

    def visitInputs_block(self, ctx: AxiomParser.Inputs_blockContext):
        return {"inputs": [self.visit(f) for f in ctx.field_def()]}

    def visitOutputs_block(self, ctx: AxiomParser.Outputs_blockContext):
        return {"outputs": [self.visit(f) for f in ctx.field_def()]}

    def visitField_def(self, ctx: AxiomParser.Field_defContext):
        d = {"name": ctx.ID().getText(), "type": self.visit(ctx.type_def())}
        if ctx.directive_block():
            d["directives"] = self.visit(ctx.directive_block())
        return d

    def visitDirective_block(self, ctx: AxiomParser.Directive_blockContext):
        return dict([self.visit(p) for p in ctx.directive_pair()])

    def visitType_def(self, ctx: AxiomParser.Type_defContext):
        return ctx.getText()

    def visitTest_case(self, ctx: AxiomParser.Test_caseContext):
        d = {"name": ctx.STRING().getText()[1:-1]}
        for field in ctx.test_field():
            d.update(self.visit(field))
        return d

    def visitInputs_test_block(self, ctx: AxiomParser.Inputs_test_blockContext):
        return {"inputs": dict([self.visit(itp) for itp in ctx.inputs_test_pair()])}

    def visitExpected_output_block(self, ctx: AxiomParser.Expected_output_blockContext):
        content = ctx.MULTILINE_CONTENT().getText()[3:-3].strip()
        return {"expected_output": json.loads(content)}

    # --- The Definitive, Correct Assertion Visitor ---
    def visitAssert_block(self, ctx: AxiomParser.Assert_blockContext):
        return {"assert": [self.visit(item) for item in ctx.assert_item()]}

    def visitAssert_item(self, ctx: AxiomParser.Assert_itemContext):
        """
        This is the new intelligent core. It parses the operator from the string.
        """
        # The grammar rule `assert_item: '-' STRING` gives us one child: the STRING token.
        full_assertion_str = ctx.STRING(0).getText()[1:-1]  # Strip outer quotes

        # Check for our custom semantic operator
        if ' ~=' in full_assertion_str:
            parts = full_assertion_str.split(' ~=', 1)
            expression = parts[0].strip()
            # The semantic part will be a string, likely with single quotes.
            # We strip whitespace and then the outer quotes (single or double).
            semantic_check = parts[1].strip()
            if semantic_check.startswith("'") and semantic_check.endswith("'"):
                semantic_check = semantic_check[1:-1]
            elif semantic_check.startswith('"') and semantic_check.endswith('"'):
                semantic_check = semantic_check[1:-1]
        else:
            # If no operator is found, it's a standard assertion.
            expression = full_assertion_str
            semantic_check = None

        return {
            "expression": expression,
            "semantic_check": semantic_check
        }

    def visitMeta_field(self, ctx: AxiomParser.Meta_fieldContext):
        return ctx.ID().getText(), ctx.STRING().getText()[1:-1]

    def visitConfig_field(self, ctx: AxiomParser.Config_fieldContext):
        return ctx.ID().getText(), self.visit(ctx.value())

    def visitDirective_pair(self, ctx: AxiomParser.Directive_pairContext):
        return ctx.ID().getText(), self.visit(ctx.value())

    def visitInputs_test_pair(self, ctx: AxiomParser.Inputs_test_pairContext):
        return ctx.ID().getText(), self.visit(ctx.value())

    def visitValue(self, ctx: AxiomParser.ValueContext):
        if ctx.STRING(): return ctx.STRING().getText()[1:-1]
        if ctx.SIGNED_NUMBER():
            num_str = ctx.SIGNED_NUMBER().getText()
            return float(num_str) if '.' in num_str else int(num_str)
        if ctx.getText() == 'true': return True
        if ctx.getText() == 'false': return False
        if ctx.json_object(): return self.visit(ctx.json_object())

    def visitJson_object(self, ctx: AxiomParser.Json_objectContext):
        obj = {}
        if ctx.json_pair():
            for pair in ctx.json_pair():
                key, value = self.visit(pair)
                obj[key] = value
        return obj

    def visitJson_pair(self, ctx: AxiomParser.Json_pairContext):
        key = ctx.STRING().getText()[1:-1]
        value = self.visit(ctx.value())
        return key, value