# Generated from axiom/parser/Axiom.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,281,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,1,2,5,2,81,
        8,2,10,2,12,2,84,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,5,5,99,8,5,10,5,12,5,102,9,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,
        1,7,5,7,112,8,7,10,7,12,7,115,9,7,1,7,1,7,1,8,1,8,1,8,3,8,122,8,
        8,1,9,1,9,1,9,5,9,127,8,9,10,9,12,9,130,9,9,1,9,1,9,1,10,1,10,1,
        10,1,10,5,10,138,8,10,10,10,12,10,141,9,10,1,10,1,10,1,11,1,11,1,
        11,5,11,148,8,11,10,11,12,11,151,9,11,1,11,1,11,1,12,1,12,1,12,5,
        12,158,8,12,10,12,12,12,161,9,12,1,12,1,12,1,13,1,13,1,13,1,13,3,
        13,169,8,13,1,13,1,13,1,13,3,13,174,8,13,1,14,1,14,1,14,1,14,5,14,
        180,8,14,10,14,12,14,183,9,14,3,14,185,8,14,1,14,1,14,1,15,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,3,16,197,8,16,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,5,18,206,8,18,10,18,12,18,209,9,18,3,18,211,8,18,
        1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,5,20,223,8,20,
        10,20,12,20,226,9,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,
        1,23,1,23,1,23,5,23,240,8,23,10,23,12,23,243,9,23,1,23,1,23,1,24,
        1,24,1,24,1,24,5,24,251,8,24,10,24,12,24,254,9,24,1,24,1,24,1,25,
        1,25,3,25,260,8,25,1,26,1,26,1,26,5,26,265,8,26,10,26,12,26,268,
        9,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,
        0,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,0,2,1,0,16,19,2,0,29,30,32,33,280,0,63,
        1,0,0,0,2,75,1,0,0,0,4,77,1,0,0,0,6,87,1,0,0,0,8,91,1,0,0,0,10,95,
        1,0,0,0,12,105,1,0,0,0,14,108,1,0,0,0,16,121,1,0,0,0,18,123,1,0,
        0,0,20,133,1,0,0,0,22,144,1,0,0,0,24,154,1,0,0,0,26,164,1,0,0,0,
        28,175,1,0,0,0,30,188,1,0,0,0,32,196,1,0,0,0,34,198,1,0,0,0,36,200,
        1,0,0,0,38,214,1,0,0,0,40,219,1,0,0,0,42,229,1,0,0,0,44,233,1,0,
        0,0,46,236,1,0,0,0,48,246,1,0,0,0,50,259,1,0,0,0,52,261,1,0,0,0,
        54,271,1,0,0,0,56,275,1,0,0,0,58,278,1,0,0,0,60,62,3,2,1,0,61,60,
        1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,
        65,63,1,0,0,0,66,67,5,0,0,1,67,1,1,0,0,0,68,76,3,4,2,0,69,76,3,8,
        4,0,70,76,3,10,5,0,71,76,3,14,7,0,72,76,3,40,20,0,73,76,3,44,22,
        0,74,76,3,46,23,0,75,68,1,0,0,0,75,69,1,0,0,0,75,70,1,0,0,0,75,71,
        1,0,0,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,3,1,0,0,0,77,
        78,5,1,0,0,78,82,5,2,0,0,79,81,3,6,3,0,80,79,1,0,0,0,81,84,1,0,0,
        0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,
        5,3,0,0,86,5,1,0,0,0,87,88,5,31,0,0,88,89,5,4,0,0,89,90,5,32,0,0,
        90,7,1,0,0,0,91,92,5,5,0,0,92,93,5,4,0,0,93,94,5,32,0,0,94,9,1,0,
        0,0,95,96,5,6,0,0,96,100,5,2,0,0,97,99,3,12,6,0,98,97,1,0,0,0,99,
        102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,
        1,0,0,0,103,104,5,3,0,0,104,11,1,0,0,0,105,106,5,7,0,0,106,107,5,
        32,0,0,107,13,1,0,0,0,108,109,5,8,0,0,109,113,5,2,0,0,110,112,3,
        16,8,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,
        0,0,0,114,116,1,0,0,0,115,113,1,0,0,0,116,117,5,3,0,0,117,15,1,0,
        0,0,118,122,3,18,9,0,119,122,3,22,11,0,120,122,3,24,12,0,121,118,
        1,0,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,17,1,0,0,0,123,124,5,
        9,0,0,124,128,5,2,0,0,125,127,3,20,10,0,126,125,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,128,
        1,0,0,0,131,132,5,3,0,0,132,19,1,0,0,0,133,134,5,10,0,0,134,135,
        5,31,0,0,135,139,5,2,0,0,136,138,3,26,13,0,137,136,1,0,0,0,138,141,
        1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,
        1,0,0,0,142,143,5,3,0,0,143,21,1,0,0,0,144,145,5,11,0,0,145,149,
        5,2,0,0,146,148,3,26,13,0,147,146,1,0,0,0,148,151,1,0,0,0,149,147,
        1,0,0,0,149,150,1,0,0,0,150,152,1,0,0,0,151,149,1,0,0,0,152,153,
        5,3,0,0,153,23,1,0,0,0,154,155,5,12,0,0,155,159,5,2,0,0,156,158,
        3,26,13,0,157,156,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,
        1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,163,5,3,0,0,163,25,1,
        0,0,0,164,165,5,31,0,0,165,166,5,4,0,0,166,168,3,32,16,0,167,169,
        3,28,14,0,168,167,1,0,0,0,168,169,1,0,0,0,169,173,1,0,0,0,170,171,
        5,31,0,0,171,172,5,4,0,0,172,174,5,32,0,0,173,170,1,0,0,0,173,174,
        1,0,0,0,174,27,1,0,0,0,175,184,5,13,0,0,176,181,3,30,15,0,177,178,
        5,14,0,0,178,180,3,30,15,0,179,177,1,0,0,0,180,183,1,0,0,0,181,179,
        1,0,0,0,181,182,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,184,176,
        1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,187,5,15,0,0,187,29,
        1,0,0,0,188,189,5,31,0,0,189,190,5,4,0,0,190,191,3,58,29,0,191,31,
        1,0,0,0,192,197,3,34,17,0,193,197,5,31,0,0,194,197,3,36,18,0,195,
        197,3,38,19,0,196,192,1,0,0,0,196,193,1,0,0,0,196,194,1,0,0,0,196,
        195,1,0,0,0,197,33,1,0,0,0,198,199,7,0,0,0,199,35,1,0,0,0,200,201,
        5,20,0,0,201,210,5,13,0,0,202,207,5,32,0,0,203,204,5,14,0,0,204,
        206,5,32,0,0,205,203,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,
        208,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,210,202,1,0,0,0,210,
        211,1,0,0,0,211,212,1,0,0,0,212,213,5,15,0,0,213,37,1,0,0,0,214,
        215,5,21,0,0,215,216,5,22,0,0,216,217,3,32,16,0,217,218,5,23,0,0,
        218,39,1,0,0,0,219,220,5,24,0,0,220,224,5,2,0,0,221,223,3,42,21,
        0,222,221,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,
        0,225,227,1,0,0,0,226,224,1,0,0,0,227,228,5,3,0,0,228,41,1,0,0,0,
        229,230,5,31,0,0,230,231,5,4,0,0,231,232,3,58,29,0,232,43,1,0,0,
        0,233,234,5,25,0,0,234,235,5,34,0,0,235,45,1,0,0,0,236,237,5,26,
        0,0,237,241,5,2,0,0,238,240,3,48,24,0,239,238,1,0,0,0,240,243,1,
        0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,244,1,0,0,0,243,241,1,
        0,0,0,244,245,5,3,0,0,245,47,1,0,0,0,246,247,5,27,0,0,247,248,5,
        32,0,0,248,252,5,2,0,0,249,251,3,50,25,0,250,249,1,0,0,0,251,254,
        1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,255,1,0,0,0,254,252,
        1,0,0,0,255,256,5,3,0,0,256,49,1,0,0,0,257,260,3,52,26,0,258,260,
        3,56,28,0,259,257,1,0,0,0,259,258,1,0,0,0,260,51,1,0,0,0,261,262,
        5,11,0,0,262,266,5,2,0,0,263,265,3,54,27,0,264,263,1,0,0,0,265,268,
        1,0,0,0,266,264,1,0,0,0,266,267,1,0,0,0,267,269,1,0,0,0,268,266,
        1,0,0,0,269,270,5,3,0,0,270,53,1,0,0,0,271,272,5,31,0,0,272,273,
        5,4,0,0,273,274,5,32,0,0,274,55,1,0,0,0,275,276,5,28,0,0,276,277,
        5,34,0,0,277,57,1,0,0,0,278,279,7,1,0,0,279,59,1,0,0,0,22,63,75,
        82,100,113,121,128,139,149,159,168,173,181,184,196,207,210,224,241,
        252,259,266
    ]

class AxiomParser ( Parser ):

    grammarFileName = "Axiom.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'meta'", "'{'", "'}'", "':'", "'persona'", 
                     "'rules'", "'-'", "'interface'", "'types'", "'struct'", 
                     "'inputs'", "'outputs'", "'('", "','", "')'", "'String'", 
                     "'Float'", "'Int'", "'Boolean'", "'Enum'", "'List'", 
                     "'<'", "'>'", "'config'", "'payload'", "'tests'", "'test'", 
                     "'expected_output'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "KEY", "STRING", 
                      "SIGNED_NUMBER", "MULTILINE_CONTENT", "WS", "COMMENT" ]

    RULE_prompt = 0
    RULE_block = 1
    RULE_meta_block = 2
    RULE_meta_field = 3
    RULE_persona_block = 4
    RULE_rules_block = 5
    RULE_rule_item = 6
    RULE_interface_block = 7
    RULE_interface_body = 8
    RULE_types_block = 9
    RULE_struct_def = 10
    RULE_inputs_block = 11
    RULE_outputs_block = 12
    RULE_field_def = 13
    RULE_directive_block = 14
    RULE_directive_pair = 15
    RULE_type_def = 16
    RULE_primitive_type = 17
    RULE_enum_def = 18
    RULE_list_def = 19
    RULE_config_block = 20
    RULE_config_field = 21
    RULE_payload_block = 22
    RULE_tests_block = 23
    RULE_test_case = 24
    RULE_test_field = 25
    RULE_inputs_test_block = 26
    RULE_inputs_test_pair = 27
    RULE_expected_output_block = 28
    RULE_value = 29

    ruleNames =  [ "prompt", "block", "meta_block", "meta_field", "persona_block", 
                   "rules_block", "rule_item", "interface_block", "interface_body", 
                   "types_block", "struct_def", "inputs_block", "outputs_block", 
                   "field_def", "directive_block", "directive_pair", "type_def", 
                   "primitive_type", "enum_def", "list_def", "config_block", 
                   "config_field", "payload_block", "tests_block", "test_case", 
                   "test_field", "inputs_test_block", "inputs_test_pair", 
                   "expected_output_block", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    KEY=31
    STRING=32
    SIGNED_NUMBER=33
    MULTILINE_CONTENT=34
    WS=35
    COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PromptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AxiomParser.EOF, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.BlockContext)
            else:
                return self.getTypedRuleContext(AxiomParser.BlockContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_prompt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrompt" ):
                return visitor.visitPrompt(self)
            else:
                return visitor.visitChildren(self)




    def prompt(self):

        localctx = AxiomParser.PromptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prompt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 117440866) != 0):
                self.state = 60
                self.block()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(AxiomParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def meta_block(self):
            return self.getTypedRuleContext(AxiomParser.Meta_blockContext,0)


        def persona_block(self):
            return self.getTypedRuleContext(AxiomParser.Persona_blockContext,0)


        def rules_block(self):
            return self.getTypedRuleContext(AxiomParser.Rules_blockContext,0)


        def interface_block(self):
            return self.getTypedRuleContext(AxiomParser.Interface_blockContext,0)


        def config_block(self):
            return self.getTypedRuleContext(AxiomParser.Config_blockContext,0)


        def payload_block(self):
            return self.getTypedRuleContext(AxiomParser.Payload_blockContext,0)


        def tests_block(self):
            return self.getTypedRuleContext(AxiomParser.Tests_blockContext,0)


        def getRuleIndex(self):
            return AxiomParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = AxiomParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.meta_block()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.persona_block()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.rules_block()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.interface_block()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.config_block()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.payload_block()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.tests_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Meta_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def meta_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Meta_fieldContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Meta_fieldContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_meta_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeta_block" ):
                return visitor.visitMeta_block(self)
            else:
                return visitor.visitChildren(self)




    def meta_block(self):

        localctx = AxiomParser.Meta_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_meta_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(AxiomParser.T__0)
            self.state = 78
            self.match(AxiomParser.T__1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 79
                self.meta_field()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Meta_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(AxiomParser.KEY, 0)

        def STRING(self):
            return self.getToken(AxiomParser.STRING, 0)

        def getRuleIndex(self):
            return AxiomParser.RULE_meta_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeta_field" ):
                return visitor.visitMeta_field(self)
            else:
                return visitor.visitChildren(self)




    def meta_field(self):

        localctx = AxiomParser.Meta_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_meta_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(AxiomParser.KEY)
            self.state = 88
            self.match(AxiomParser.T__3)
            self.state = 89
            self.match(AxiomParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Persona_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AxiomParser.STRING, 0)

        def getRuleIndex(self):
            return AxiomParser.RULE_persona_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPersona_block" ):
                return visitor.visitPersona_block(self)
            else:
                return visitor.visitChildren(self)




    def persona_block(self):

        localctx = AxiomParser.Persona_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_persona_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(AxiomParser.T__4)
            self.state = 92
            self.match(AxiomParser.T__3)
            self.state = 93
            self.match(AxiomParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rules_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Rule_itemContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Rule_itemContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_rules_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRules_block" ):
                return visitor.visitRules_block(self)
            else:
                return visitor.visitChildren(self)




    def rules_block(self):

        localctx = AxiomParser.Rules_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rules_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(AxiomParser.T__5)
            self.state = 96
            self.match(AxiomParser.T__1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 97
                self.rule_item()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AxiomParser.STRING, 0)

        def getRuleIndex(self):
            return AxiomParser.RULE_rule_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_item" ):
                return visitor.visitRule_item(self)
            else:
                return visitor.visitChildren(self)




    def rule_item(self):

        localctx = AxiomParser.Rule_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rule_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(AxiomParser.T__6)
            self.state = 106
            self.match(AxiomParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Interface_bodyContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Interface_bodyContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_interface_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_block" ):
                return visitor.visitInterface_block(self)
            else:
                return visitor.visitChildren(self)




    def interface_block(self):

        localctx = AxiomParser.Interface_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_interface_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(AxiomParser.T__7)
            self.state = 109
            self.match(AxiomParser.T__1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6656) != 0):
                self.state = 110
                self.interface_body()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types_block(self):
            return self.getTypedRuleContext(AxiomParser.Types_blockContext,0)


        def inputs_block(self):
            return self.getTypedRuleContext(AxiomParser.Inputs_blockContext,0)


        def outputs_block(self):
            return self.getTypedRuleContext(AxiomParser.Outputs_blockContext,0)


        def getRuleIndex(self):
            return AxiomParser.RULE_interface_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_body" ):
                return visitor.visitInterface_body(self)
            else:
                return visitor.visitChildren(self)




    def interface_body(self):

        localctx = AxiomParser.Interface_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_interface_body)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.types_block()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.inputs_block()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.outputs_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Types_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Struct_defContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Struct_defContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_types_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes_block" ):
                return visitor.visitTypes_block(self)
            else:
                return visitor.visitChildren(self)




    def types_block(self):

        localctx = AxiomParser.Types_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_types_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(AxiomParser.T__8)
            self.state = 124
            self.match(AxiomParser.T__1)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 125
                self.struct_def()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(AxiomParser.KEY, 0)

        def field_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Field_defContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Field_defContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_struct_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_def" ):
                return visitor.visitStruct_def(self)
            else:
                return visitor.visitChildren(self)




    def struct_def(self):

        localctx = AxiomParser.Struct_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_struct_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(AxiomParser.T__9)
            self.state = 134
            self.match(AxiomParser.KEY)
            self.state = 135
            self.match(AxiomParser.T__1)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 136
                self.field_def()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inputs_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Field_defContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Field_defContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_inputs_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputs_block" ):
                return visitor.visitInputs_block(self)
            else:
                return visitor.visitChildren(self)




    def inputs_block(self):

        localctx = AxiomParser.Inputs_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_inputs_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(AxiomParser.T__10)
            self.state = 145
            self.match(AxiomParser.T__1)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 146
                self.field_def()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Outputs_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Field_defContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Field_defContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_outputs_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputs_block" ):
                return visitor.visitOutputs_block(self)
            else:
                return visitor.visitChildren(self)




    def outputs_block(self):

        localctx = AxiomParser.Outputs_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_outputs_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(AxiomParser.T__11)
            self.state = 155
            self.match(AxiomParser.T__1)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 156
                self.field_def()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self, i:int=None):
            if i is None:
                return self.getTokens(AxiomParser.KEY)
            else:
                return self.getToken(AxiomParser.KEY, i)

        def type_def(self):
            return self.getTypedRuleContext(AxiomParser.Type_defContext,0)


        def directive_block(self):
            return self.getTypedRuleContext(AxiomParser.Directive_blockContext,0)


        def STRING(self):
            return self.getToken(AxiomParser.STRING, 0)

        def getRuleIndex(self):
            return AxiomParser.RULE_field_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_def" ):
                return visitor.visitField_def(self)
            else:
                return visitor.visitChildren(self)




    def field_def(self):

        localctx = AxiomParser.Field_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_field_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(AxiomParser.KEY)
            self.state = 165
            self.match(AxiomParser.T__3)
            self.state = 166
            self.type_def()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 167
                self.directive_block()


            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 170
                self.match(AxiomParser.KEY)
                self.state = 171
                self.match(AxiomParser.T__3)
                self.state = 172
                self.match(AxiomParser.STRING)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Directive_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directive_pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Directive_pairContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Directive_pairContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_directive_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective_block" ):
                return visitor.visitDirective_block(self)
            else:
                return visitor.visitChildren(self)




    def directive_block(self):

        localctx = AxiomParser.Directive_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_directive_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(AxiomParser.T__12)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 176
                self.directive_pair()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 177
                    self.match(AxiomParser.T__13)
                    self.state = 178
                    self.directive_pair()
                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 186
            self.match(AxiomParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Directive_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(AxiomParser.KEY, 0)

        def value(self):
            return self.getTypedRuleContext(AxiomParser.ValueContext,0)


        def getRuleIndex(self):
            return AxiomParser.RULE_directive_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective_pair" ):
                return visitor.visitDirective_pair(self)
            else:
                return visitor.visitChildren(self)




    def directive_pair(self):

        localctx = AxiomParser.Directive_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_directive_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(AxiomParser.KEY)
            self.state = 189
            self.match(AxiomParser.T__3)
            self.state = 190
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(AxiomParser.Primitive_typeContext,0)


        def KEY(self):
            return self.getToken(AxiomParser.KEY, 0)

        def enum_def(self):
            return self.getTypedRuleContext(AxiomParser.Enum_defContext,0)


        def list_def(self):
            return self.getTypedRuleContext(AxiomParser.List_defContext,0)


        def getRuleIndex(self):
            return AxiomParser.RULE_type_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_def" ):
                return visitor.visitType_def(self)
            else:
                return visitor.visitChildren(self)




    def type_def(self):

        localctx = AxiomParser.Type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_type_def)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.primitive_type()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(AxiomParser.KEY)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.enum_def()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.list_def()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AxiomParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = AxiomParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(AxiomParser.STRING)
            else:
                return self.getToken(AxiomParser.STRING, i)

        def getRuleIndex(self):
            return AxiomParser.RULE_enum_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum_def" ):
                return visitor.visitEnum_def(self)
            else:
                return visitor.visitChildren(self)




    def enum_def(self):

        localctx = AxiomParser.Enum_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_enum_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(AxiomParser.T__19)
            self.state = 201
            self.match(AxiomParser.T__12)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 202
                self.match(AxiomParser.STRING)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 203
                    self.match(AxiomParser.T__13)
                    self.state = 204
                    self.match(AxiomParser.STRING)
                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 212
            self.match(AxiomParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(AxiomParser.Type_defContext,0)


        def getRuleIndex(self):
            return AxiomParser.RULE_list_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_def" ):
                return visitor.visitList_def(self)
            else:
                return visitor.visitChildren(self)




    def list_def(self):

        localctx = AxiomParser.List_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(AxiomParser.T__20)
            self.state = 215
            self.match(AxiomParser.T__21)
            self.state = 216
            self.type_def()
            self.state = 217
            self.match(AxiomParser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Config_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def config_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Config_fieldContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Config_fieldContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_config_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfig_block" ):
                return visitor.visitConfig_block(self)
            else:
                return visitor.visitChildren(self)




    def config_block(self):

        localctx = AxiomParser.Config_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_config_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(AxiomParser.T__23)
            self.state = 220
            self.match(AxiomParser.T__1)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 221
                self.config_field()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Config_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(AxiomParser.KEY, 0)

        def value(self):
            return self.getTypedRuleContext(AxiomParser.ValueContext,0)


        def getRuleIndex(self):
            return AxiomParser.RULE_config_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfig_field" ):
                return visitor.visitConfig_field(self)
            else:
                return visitor.visitChildren(self)




    def config_field(self):

        localctx = AxiomParser.Config_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_config_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(AxiomParser.KEY)
            self.state = 230
            self.match(AxiomParser.T__3)
            self.state = 231
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Payload_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTILINE_CONTENT(self):
            return self.getToken(AxiomParser.MULTILINE_CONTENT, 0)

        def getRuleIndex(self):
            return AxiomParser.RULE_payload_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayload_block" ):
                return visitor.visitPayload_block(self)
            else:
                return visitor.visitChildren(self)




    def payload_block(self):

        localctx = AxiomParser.Payload_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_payload_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(AxiomParser.T__24)
            self.state = 234
            self.match(AxiomParser.MULTILINE_CONTENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tests_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test_case(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Test_caseContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Test_caseContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_tests_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTests_block" ):
                return visitor.visitTests_block(self)
            else:
                return visitor.visitChildren(self)




    def tests_block(self):

        localctx = AxiomParser.Tests_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_tests_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(AxiomParser.T__25)
            self.state = 237
            self.match(AxiomParser.T__1)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 238
                self.test_case()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Test_caseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AxiomParser.STRING, 0)

        def test_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Test_fieldContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Test_fieldContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_test_case

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTest_case" ):
                return visitor.visitTest_case(self)
            else:
                return visitor.visitChildren(self)




    def test_case(self):

        localctx = AxiomParser.Test_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_test_case)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(AxiomParser.T__26)
            self.state = 247
            self.match(AxiomParser.STRING)
            self.state = 248
            self.match(AxiomParser.T__1)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==28:
                self.state = 249
                self.test_field()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 255
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Test_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inputs_test_block(self):
            return self.getTypedRuleContext(AxiomParser.Inputs_test_blockContext,0)


        def expected_output_block(self):
            return self.getTypedRuleContext(AxiomParser.Expected_output_blockContext,0)


        def getRuleIndex(self):
            return AxiomParser.RULE_test_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTest_field" ):
                return visitor.visitTest_field(self)
            else:
                return visitor.visitChildren(self)




    def test_field(self):

        localctx = AxiomParser.Test_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_test_field)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.inputs_test_block()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.expected_output_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inputs_test_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inputs_test_pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AxiomParser.Inputs_test_pairContext)
            else:
                return self.getTypedRuleContext(AxiomParser.Inputs_test_pairContext,i)


        def getRuleIndex(self):
            return AxiomParser.RULE_inputs_test_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputs_test_block" ):
                return visitor.visitInputs_test_block(self)
            else:
                return visitor.visitChildren(self)




    def inputs_test_block(self):

        localctx = AxiomParser.Inputs_test_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_inputs_test_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(AxiomParser.T__10)
            self.state = 262
            self.match(AxiomParser.T__1)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 263
                self.inputs_test_pair()
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 269
            self.match(AxiomParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inputs_test_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(AxiomParser.KEY, 0)

        def STRING(self):
            return self.getToken(AxiomParser.STRING, 0)

        def getRuleIndex(self):
            return AxiomParser.RULE_inputs_test_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputs_test_pair" ):
                return visitor.visitInputs_test_pair(self)
            else:
                return visitor.visitChildren(self)




    def inputs_test_pair(self):

        localctx = AxiomParser.Inputs_test_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_inputs_test_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(AxiomParser.KEY)
            self.state = 272
            self.match(AxiomParser.T__3)
            self.state = 273
            self.match(AxiomParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expected_output_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTILINE_CONTENT(self):
            return self.getToken(AxiomParser.MULTILINE_CONTENT, 0)

        def getRuleIndex(self):
            return AxiomParser.RULE_expected_output_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpected_output_block" ):
                return visitor.visitExpected_output_block(self)
            else:
                return visitor.visitChildren(self)




    def expected_output_block(self):

        localctx = AxiomParser.Expected_output_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expected_output_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(AxiomParser.T__27)
            self.state = 276
            self.match(AxiomParser.MULTILINE_CONTENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AxiomParser.STRING, 0)

        def SIGNED_NUMBER(self):
            return self.getToken(AxiomParser.SIGNED_NUMBER, 0)

        def getRuleIndex(self):
            return AxiomParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = AxiomParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14495514624) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





