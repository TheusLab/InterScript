# Generated from InterScriptParser.g4 by ANTLR 4.13.1
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
        4,1,31,174,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,47,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,66,8,3,10,3,12,3,69,9,3,
        1,3,1,3,1,4,1,4,1,4,5,4,76,8,4,10,4,12,4,79,9,4,1,4,3,4,82,8,4,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,94,8,6,10,6,12,6,97,9,
        6,1,6,1,6,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,1,6,3,6,109,8,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,120,8,7,10,7,12,7,123,9,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,138,
        8,10,10,10,12,10,141,9,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,3,12,152,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,
        162,8,14,10,14,12,14,165,9,14,1,14,3,14,168,8,14,1,15,1,15,1,16,
        1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,
        2,1,0,17,24,2,0,7,8,28,29,175,0,37,1,0,0,0,2,46,1,0,0,0,4,48,1,0,
        0,0,6,56,1,0,0,0,8,81,1,0,0,0,10,83,1,0,0,0,12,87,1,0,0,0,14,110,
        1,0,0,0,16,126,1,0,0,0,18,130,1,0,0,0,20,133,1,0,0,0,22,142,1,0,
        0,0,24,151,1,0,0,0,26,153,1,0,0,0,28,167,1,0,0,0,30,169,1,0,0,0,
        32,171,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,
        0,0,0,37,38,1,0,0,0,38,1,1,0,0,0,39,37,1,0,0,0,40,47,3,4,2,0,41,
        47,3,6,3,0,42,47,3,12,6,0,43,47,3,14,7,0,44,47,3,16,8,0,45,47,3,
        18,9,0,46,40,1,0,0,0,46,41,1,0,0,0,46,42,1,0,0,0,46,43,1,0,0,0,46,
        44,1,0,0,0,46,45,1,0,0,0,47,3,1,0,0,0,48,49,5,1,0,0,49,50,5,30,0,
        0,50,51,5,9,0,0,51,52,3,32,16,0,52,53,5,16,0,0,53,54,3,20,10,0,54,
        55,5,10,0,0,55,5,1,0,0,0,56,57,5,2,0,0,57,58,5,30,0,0,58,59,5,12,
        0,0,59,60,3,8,4,0,60,61,5,13,0,0,61,62,5,9,0,0,62,63,3,32,16,0,63,
        67,5,14,0,0,64,66,3,2,1,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,
        0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,5,15,0,0,71,
        7,1,0,0,0,72,77,3,10,5,0,73,74,5,11,0,0,74,76,3,10,5,0,75,73,1,0,
        0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,82,1,0,0,0,79,77,
        1,0,0,0,80,82,1,0,0,0,81,72,1,0,0,0,81,80,1,0,0,0,82,9,1,0,0,0,83,
        84,5,30,0,0,84,85,5,9,0,0,85,86,3,32,16,0,86,11,1,0,0,0,87,88,5,
        3,0,0,88,89,5,12,0,0,89,90,3,20,10,0,90,91,5,13,0,0,91,95,5,14,0,
        0,92,94,3,2,1,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,
        1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,108,5,15,0,0,99,100,5,4,0,
        0,100,104,5,14,0,0,101,103,3,2,1,0,102,101,1,0,0,0,103,106,1,0,0,
        0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,104,1,0,0,
        0,107,109,5,15,0,0,108,99,1,0,0,0,108,109,1,0,0,0,109,13,1,0,0,0,
        110,111,5,5,0,0,111,112,5,12,0,0,112,113,3,4,2,0,113,114,3,20,10,
        0,114,115,5,10,0,0,115,116,3,20,10,0,116,117,5,13,0,0,117,121,5,
        14,0,0,118,120,3,2,1,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,1,
        0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,125,5,
        15,0,0,125,15,1,0,0,0,126,127,5,6,0,0,127,128,3,20,10,0,128,129,
        5,10,0,0,129,17,1,0,0,0,130,131,3,20,10,0,131,132,5,10,0,0,132,19,
        1,0,0,0,133,139,3,24,12,0,134,135,3,22,11,0,135,136,3,24,12,0,136,
        138,1,0,0,0,137,134,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,
        140,1,0,0,0,140,21,1,0,0,0,141,139,1,0,0,0,142,143,7,0,0,0,143,23,
        1,0,0,0,144,152,5,30,0,0,145,152,3,30,15,0,146,152,3,26,13,0,147,
        148,5,12,0,0,148,149,3,20,10,0,149,150,5,13,0,0,150,152,1,0,0,0,
        151,144,1,0,0,0,151,145,1,0,0,0,151,146,1,0,0,0,151,147,1,0,0,0,
        152,25,1,0,0,0,153,154,5,30,0,0,154,155,5,12,0,0,155,156,3,28,14,
        0,156,157,5,13,0,0,157,27,1,0,0,0,158,163,3,20,10,0,159,160,5,11,
        0,0,160,162,3,20,10,0,161,159,1,0,0,0,162,165,1,0,0,0,163,161,1,
        0,0,0,163,164,1,0,0,0,164,168,1,0,0,0,165,163,1,0,0,0,166,168,1,
        0,0,0,167,158,1,0,0,0,167,166,1,0,0,0,168,29,1,0,0,0,169,170,7,1,
        0,0,170,31,1,0,0,0,171,172,5,30,0,0,172,33,1,0,0,0,13,37,46,67,77,
        81,95,104,108,121,139,151,163,167
    ]

class InterScriptParser ( Parser ):

    grammarFileName = "InterScriptParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'function'", "'if'", "'else'", 
                     "'for'", "'return'", "'true'", "'false'", "':'", "';'", 
                     "','", "'('", "')'", "'{'", "'}'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'>'", "'<'", "'=='", "'!='", "'&&'", 
                     "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "LET", "FUNCTION", "IF", "ELSE", "FOR", 
                      "RETURN", "TRUE", "FALSE", "COLON", "SEMICOLON", "COMMA", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "ASSIGN", 
                      "PLUS", "MINUS", "STAR", "SLASH", "GT", "LT", "EQ", 
                      "NEQ", "AND", "OR", "NOT", "INT", "STRING", "IDENTIFIER", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_functionDeclaration = 3
    RULE_parameterList = 4
    RULE_parameter = 5
    RULE_ifStatement = 6
    RULE_forStatement = 7
    RULE_returnStatement = 8
    RULE_expressionStatement = 9
    RULE_expression = 10
    RULE_binaryOp = 11
    RULE_primaryExpr = 12
    RULE_functionCall = 13
    RULE_argumentList = 14
    RULE_literal = 15
    RULE_type = 16

    ruleNames =  [ "program", "statement", "variableDeclaration", "functionDeclaration", 
                   "parameterList", "parameter", "ifStatement", "forStatement", 
                   "returnStatement", "expressionStatement", "expression", 
                   "binaryOp", "primaryExpr", "functionCall", "argumentList", 
                   "literal", "type" ]

    EOF = Token.EOF
    LET=1
    FUNCTION=2
    IF=3
    ELSE=4
    FOR=5
    RETURN=6
    TRUE=7
    FALSE=8
    COLON=9
    SEMICOLON=10
    COMMA=11
    LPAREN=12
    RPAREN=13
    LBRACE=14
    RBRACE=15
    ASSIGN=16
    PLUS=17
    MINUS=18
    STAR=19
    SLASH=20
    GT=21
    LT=22
    EQ=23
    NEQ=24
    AND=25
    OR=26
    NOT=27
    INT=28
    STRING=29
    IDENTIFIER=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(InterScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return InterScriptParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = InterScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879052782) != 0):
                self.state = 34
                self.statement()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(InterScriptParser.VariableDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(InterScriptParser.FunctionDeclarationContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(InterScriptParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(InterScriptParser.ForStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(InterScriptParser.ReturnStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(InterScriptParser.ExpressionStatementContext,0)


        def getRuleIndex(self):
            return InterScriptParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = InterScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.variableDeclaration()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.functionDeclaration()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.ifStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.forStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.returnStatement()
                pass
            elif token in [7, 8, 12, 28, 29, 30]:
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.expressionStatement()
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


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(InterScriptParser.LET, 0)

        def IDENTIFIER(self):
            return self.getToken(InterScriptParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(InterScriptParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(InterScriptParser.TypeContext,0)


        def ASSIGN(self):
            return self.getToken(InterScriptParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(InterScriptParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(InterScriptParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return InterScriptParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = InterScriptParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(InterScriptParser.LET)
            self.state = 49
            self.match(InterScriptParser.IDENTIFIER)
            self.state = 50
            self.match(InterScriptParser.COLON)
            self.state = 51
            self.type_()
            self.state = 52
            self.match(InterScriptParser.ASSIGN)
            self.state = 53
            self.expression()
            self.state = 54
            self.match(InterScriptParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(InterScriptParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(InterScriptParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(InterScriptParser.LPAREN, 0)

        def parameterList(self):
            return self.getTypedRuleContext(InterScriptParser.ParameterListContext,0)


        def RPAREN(self):
            return self.getToken(InterScriptParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(InterScriptParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(InterScriptParser.TypeContext,0)


        def LBRACE(self):
            return self.getToken(InterScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(InterScriptParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(InterScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return InterScriptParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = InterScriptParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(InterScriptParser.FUNCTION)
            self.state = 57
            self.match(InterScriptParser.IDENTIFIER)
            self.state = 58
            self.match(InterScriptParser.LPAREN)
            self.state = 59
            self.parameterList()
            self.state = 60
            self.match(InterScriptParser.RPAREN)
            self.state = 61
            self.match(InterScriptParser.COLON)
            self.state = 62
            self.type_()
            self.state = 63
            self.match(InterScriptParser.LBRACE)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879052782) != 0):
                self.state = 64
                self.statement()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(InterScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterScriptParser.ParameterContext)
            else:
                return self.getTypedRuleContext(InterScriptParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(InterScriptParser.COMMA)
            else:
                return self.getToken(InterScriptParser.COMMA, i)

        def getRuleIndex(self):
            return InterScriptParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = InterScriptParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.parameter()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 73
                    self.match(InterScriptParser.COMMA)
                    self.state = 74
                    self.parameter()
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)

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


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(InterScriptParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(InterScriptParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(InterScriptParser.TypeContext,0)


        def getRuleIndex(self):
            return InterScriptParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = InterScriptParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(InterScriptParser.IDENTIFIER)
            self.state = 84
            self.match(InterScriptParser.COLON)
            self.state = 85
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(InterScriptParser.IF, 0)

        def LPAREN(self):
            return self.getToken(InterScriptParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(InterScriptParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(InterScriptParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(InterScriptParser.LBRACE)
            else:
                return self.getToken(InterScriptParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(InterScriptParser.RBRACE)
            else:
                return self.getToken(InterScriptParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(InterScriptParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(InterScriptParser.ELSE, 0)

        def getRuleIndex(self):
            return InterScriptParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = InterScriptParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(InterScriptParser.IF)
            self.state = 88
            self.match(InterScriptParser.LPAREN)
            self.state = 89
            self.expression()
            self.state = 90
            self.match(InterScriptParser.RPAREN)
            self.state = 91
            self.match(InterScriptParser.LBRACE)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879052782) != 0):
                self.state = 92
                self.statement()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(InterScriptParser.RBRACE)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 99
                self.match(InterScriptParser.ELSE)
                self.state = 100
                self.match(InterScriptParser.LBRACE)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879052782) != 0):
                    self.state = 101
                    self.statement()
                    self.state = 106
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 107
                self.match(InterScriptParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(InterScriptParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(InterScriptParser.LPAREN, 0)

        def variableDeclaration(self):
            return self.getTypedRuleContext(InterScriptParser.VariableDeclarationContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(InterScriptParser.ExpressionContext,i)


        def SEMICOLON(self):
            return self.getToken(InterScriptParser.SEMICOLON, 0)

        def RPAREN(self):
            return self.getToken(InterScriptParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(InterScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(InterScriptParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(InterScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return InterScriptParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = InterScriptParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(InterScriptParser.FOR)
            self.state = 111
            self.match(InterScriptParser.LPAREN)
            self.state = 112
            self.variableDeclaration()
            self.state = 113
            self.expression()
            self.state = 114
            self.match(InterScriptParser.SEMICOLON)
            self.state = 115
            self.expression()
            self.state = 116
            self.match(InterScriptParser.RPAREN)
            self.state = 117
            self.match(InterScriptParser.LBRACE)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879052782) != 0):
                self.state = 118
                self.statement()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(InterScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(InterScriptParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(InterScriptParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(InterScriptParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return InterScriptParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = InterScriptParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(InterScriptParser.RETURN)
            self.state = 127
            self.expression()
            self.state = 128
            self.match(InterScriptParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(InterScriptParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(InterScriptParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return InterScriptParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = InterScriptParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.expression()
            self.state = 131
            self.match(InterScriptParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterScriptParser.PrimaryExprContext)
            else:
                return self.getTypedRuleContext(InterScriptParser.PrimaryExprContext,i)


        def binaryOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterScriptParser.BinaryOpContext)
            else:
                return self.getTypedRuleContext(InterScriptParser.BinaryOpContext,i)


        def getRuleIndex(self):
            return InterScriptParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = InterScriptParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.primaryExpr()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33423360) != 0):
                self.state = 134
                self.binaryOp()
                self.state = 135
                self.primaryExpr()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(InterScriptParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(InterScriptParser.MINUS, 0)

        def STAR(self):
            return self.getToken(InterScriptParser.STAR, 0)

        def SLASH(self):
            return self.getToken(InterScriptParser.SLASH, 0)

        def GT(self):
            return self.getToken(InterScriptParser.GT, 0)

        def LT(self):
            return self.getToken(InterScriptParser.LT, 0)

        def EQ(self):
            return self.getToken(InterScriptParser.EQ, 0)

        def NEQ(self):
            return self.getToken(InterScriptParser.NEQ, 0)

        def getRuleIndex(self):
            return InterScriptParser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)




    def binaryOp(self):

        localctx = InterScriptParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33423360) != 0)):
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


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(InterScriptParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(InterScriptParser.LiteralContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(InterScriptParser.FunctionCallContext,0)


        def LPAREN(self):
            return self.getToken(InterScriptParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(InterScriptParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(InterScriptParser.RPAREN, 0)

        def getRuleIndex(self):
            return InterScriptParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = InterScriptParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primaryExpr)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(InterScriptParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.match(InterScriptParser.LPAREN)
                self.state = 148
                self.expression()
                self.state = 149
                self.match(InterScriptParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(InterScriptParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(InterScriptParser.LPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(InterScriptParser.ArgumentListContext,0)


        def RPAREN(self):
            return self.getToken(InterScriptParser.RPAREN, 0)

        def getRuleIndex(self):
            return InterScriptParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = InterScriptParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(InterScriptParser.IDENTIFIER)
            self.state = 154
            self.match(InterScriptParser.LPAREN)
            self.state = 155
            self.argumentList()
            self.state = 156
            self.match(InterScriptParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(InterScriptParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(InterScriptParser.COMMA)
            else:
                return self.getToken(InterScriptParser.COMMA, i)

        def getRuleIndex(self):
            return InterScriptParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = InterScriptParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 12, 28, 29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.expression()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 159
                    self.match(InterScriptParser.COMMA)
                    self.state = 160
                    self.expression()
                    self.state = 165
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)

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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(InterScriptParser.INT, 0)

        def STRING(self):
            return self.getToken(InterScriptParser.STRING, 0)

        def TRUE(self):
            return self.getToken(InterScriptParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(InterScriptParser.FALSE, 0)

        def getRuleIndex(self):
            return InterScriptParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = InterScriptParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 805306752) != 0)):
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


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(InterScriptParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return InterScriptParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = InterScriptParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(InterScriptParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





