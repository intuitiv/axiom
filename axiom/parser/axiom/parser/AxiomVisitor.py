# Generated from axiom/parser/Axiom.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AxiomParser import AxiomParser
else:
    from AxiomParser import AxiomParser

# This class defines a complete generic visitor for a parse tree produced by AxiomParser.

class AxiomVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AxiomParser#prompt.
    def visitPrompt(self, ctx:AxiomParser.PromptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#block.
    def visitBlock(self, ctx:AxiomParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#meta_block.
    def visitMeta_block(self, ctx:AxiomParser.Meta_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#meta_field.
    def visitMeta_field(self, ctx:AxiomParser.Meta_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#persona_block.
    def visitPersona_block(self, ctx:AxiomParser.Persona_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#rules_block.
    def visitRules_block(self, ctx:AxiomParser.Rules_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#rule_item.
    def visitRule_item(self, ctx:AxiomParser.Rule_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#interface_block.
    def visitInterface_block(self, ctx:AxiomParser.Interface_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#interface_body.
    def visitInterface_body(self, ctx:AxiomParser.Interface_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#types_block.
    def visitTypes_block(self, ctx:AxiomParser.Types_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#struct_def.
    def visitStruct_def(self, ctx:AxiomParser.Struct_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#inputs_block.
    def visitInputs_block(self, ctx:AxiomParser.Inputs_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#outputs_block.
    def visitOutputs_block(self, ctx:AxiomParser.Outputs_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#field_def.
    def visitField_def(self, ctx:AxiomParser.Field_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#directive_block.
    def visitDirective_block(self, ctx:AxiomParser.Directive_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#directive_pair.
    def visitDirective_pair(self, ctx:AxiomParser.Directive_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#type_def.
    def visitType_def(self, ctx:AxiomParser.Type_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#primitive_type.
    def visitPrimitive_type(self, ctx:AxiomParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#enum_def.
    def visitEnum_def(self, ctx:AxiomParser.Enum_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#list_def.
    def visitList_def(self, ctx:AxiomParser.List_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#config_block.
    def visitConfig_block(self, ctx:AxiomParser.Config_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#config_field.
    def visitConfig_field(self, ctx:AxiomParser.Config_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#payload_block.
    def visitPayload_block(self, ctx:AxiomParser.Payload_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#tests_block.
    def visitTests_block(self, ctx:AxiomParser.Tests_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#test_case.
    def visitTest_case(self, ctx:AxiomParser.Test_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#test_field.
    def visitTest_field(self, ctx:AxiomParser.Test_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#inputs_test_block.
    def visitInputs_test_block(self, ctx:AxiomParser.Inputs_test_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#inputs_test_pair.
    def visitInputs_test_pair(self, ctx:AxiomParser.Inputs_test_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#expected_output_block.
    def visitExpected_output_block(self, ctx:AxiomParser.Expected_output_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AxiomParser#value.
    def visitValue(self, ctx:AxiomParser.ValueContext):
        return self.visitChildren(ctx)



del AxiomParser