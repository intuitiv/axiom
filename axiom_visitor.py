import json
from AxiomParser import AxiomParser
from AxiomVisitor import AxiomVisitor


class AxiomVisitorImpl(AxiomVisitor):
    def visitPrompt(self, ctx: AxiomParser.PromptContext):
        prompt_dict = {}
        for block_ctx in ctx.block():
            block_result = self.visit(block_ctx)
            if block_result:
                prompt_dict.update(block_result)
        return prompt_dict

    def visitMeta_block(self, ctx: AxiomParser.Meta_blockContext):
        return {"meta": dict([self.visit(mf) for mf in ctx.meta_field()])}

    def visitMeta_field(self, ctx: AxiomParser.Meta_fieldContext):
        return ctx.KEY().getText(), ctx.STRING().getText()[1:-1]

    def visitPersona_block(self, ctx: AxiomParser.Persona_blockContext):
        return {"persona": ctx.STRING().getText()[1:-1]}

    def visitRules_block(self, ctx: AxiomParser.Rules_blockContext):
        return {"rules": [self.visit(r) for r in ctx.rule_item()]}

    def visitRule_item(self, ctx: AxiomParser.Rule_itemContext):
        return ctx.STRING().getText()[1:-1]

    def visitInterface_block(self, ctx: AxiomParser.Interface_blockContext):
        interface_dict = {}
        for body in ctx.interface_body():
            interface_dict.update(self.visit(body))
        return {"interface": interface_dict}

    def visitTypes_block(self, ctx: AxiomParser.Types_blockContext):
        return {"types": dict([self.visit(s) for s in ctx.struct_def()])}

    def visitStruct_def(self, ctx: AxiomParser.Struct_defContext):
        key = ctx.KEY().getText()
        fields = [self.visit(f) for f in ctx.field_def()]
        return key, fields

    def visitInputs_block(self, ctx: AxiomParser.Inputs_blockContext):
        return {"inputs": [self.visit(f) for f in ctx.field_def()]}

    def visitOutputs_block(self, ctx: AxiomParser.Outputs_blockContext):
        return {"outputs": [self.visit(f) for f in ctx.field_def()]}

    # CORRECTED Visitor for the unambiguous field_def rule
    def visitField_def(self, ctx: AxiomParser.Field_defContext):
        # The first KEY is the field name
        d = {"name": ctx.KEY(0).getText(), "type": self.visit(ctx.type_def())}
        if ctx.directive_block():
            d["directives"] = self.visit(ctx.directive_block())
        # If there's a second KEY, it must be the description
        if ctx.KEY(1):
            if ctx.KEY(1).getText() == "description":
                d["description"] = ctx.STRING().getText()[1:-1]
        return d

    def visitDirective_block(self, ctx: AxiomParser.Directive_blockContext):
        return dict([self.visit(p) for p in ctx.directive_pair()])

    def visitDirective_pair(self, ctx: AxiomParser.Directive_pairContext):
        return ctx.KEY().getText(), self.visit(ctx.value())

    def visitType_def(self, ctx: AxiomParser.Type_defContext):
        return ctx.getText()

    def visitConfig_block(self, ctx: AxiomParser.Config_blockContext):
        return {"config": dict([self.visit(cf) for cf in ctx.config_field()])}

    def visitConfig_field(self, ctx: AxiomParser.Config_fieldContext):
        return ctx.KEY().getText(), self.visit(ctx.value())

    def visitValue(self, ctx: AxiomParser.ValueContext):
        if ctx.STRING(): return ctx.STRING().getText()[1:-1]
        if ctx.SIGNED_NUMBER():
            num_str = ctx.SIGNED_NUMBER().getText()
            return float(num_str) if '.' in num_str else int(num_str)
        if ctx.getText() == 'true': return True
        if ctx.getText() == 'false': return False

    def visitPayload_block(self, ctx: AxiomParser.Payload_blockContext):
        content = ctx.MULTILINE_CONTENT().getText()
        return {"payload": content[3:-3].strip()}

    def visitTests_block(self, ctx: AxiomParser.Tests_blockContext):
        return {"tests": [self.visit(tc) for tc in ctx.test_case()]}

    def visitTest_case(self, ctx: AxiomParser.Test_caseContext):
        d = {"name": ctx.STRING().getText()[1:-1]}
        for field in ctx.test_field():
            d.update(self.visit(field))
        return d

    def visitInputs_test_block(self, ctx: AxiomParser.Inputs_test_blockContext):
        return {"inputs": dict([self.visit(itp) for itp in ctx.inputs_test_pair()])}

    def visitInputs_test_pair(self, ctx: AxiomParser.Inputs_test_pairContext):
        return ctx.KEY().getText(), ctx.STRING().getText()[1:-1]

    def visitExpected_output_block(self, ctx: AxiomParser.Expected_output_blockContext):
        content = ctx.MULTILINE_CONTENT().getText()[3:-3].strip()
        return {"expected_output": json.loads(content)}