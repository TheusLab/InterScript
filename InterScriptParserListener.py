# Generated from InterScriptParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .InterScriptParser import InterScriptParser
else:
    from InterScriptParser import InterScriptParser

# This class defines a complete listener for a parse tree produced by InterScriptParser.
class InterScriptParserListener(ParseTreeListener):

    # Enter a parse tree produced by InterScriptParser#program.
    def enterProgram(self, ctx:InterScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by InterScriptParser#program.
    def exitProgram(self, ctx:InterScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by InterScriptParser#statement.
    def enterStatement(self, ctx:InterScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by InterScriptParser#statement.
    def exitStatement(self, ctx:InterScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by InterScriptParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:InterScriptParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by InterScriptParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:InterScriptParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by InterScriptParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:InterScriptParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by InterScriptParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:InterScriptParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by InterScriptParser#parameterList.
    def enterParameterList(self, ctx:InterScriptParser.ParameterListContext):
        pass

    # Exit a parse tree produced by InterScriptParser#parameterList.
    def exitParameterList(self, ctx:InterScriptParser.ParameterListContext):
        pass


    # Enter a parse tree produced by InterScriptParser#parameter.
    def enterParameter(self, ctx:InterScriptParser.ParameterContext):
        pass

    # Exit a parse tree produced by InterScriptParser#parameter.
    def exitParameter(self, ctx:InterScriptParser.ParameterContext):
        pass


    # Enter a parse tree produced by InterScriptParser#ifStatement.
    def enterIfStatement(self, ctx:InterScriptParser.IfStatementContext):
        pass

    # Exit a parse tree produced by InterScriptParser#ifStatement.
    def exitIfStatement(self, ctx:InterScriptParser.IfStatementContext):
        pass


    # Enter a parse tree produced by InterScriptParser#forStatement.
    def enterForStatement(self, ctx:InterScriptParser.ForStatementContext):
        pass

    # Exit a parse tree produced by InterScriptParser#forStatement.
    def exitForStatement(self, ctx:InterScriptParser.ForStatementContext):
        pass


    # Enter a parse tree produced by InterScriptParser#returnStatement.
    def enterReturnStatement(self, ctx:InterScriptParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by InterScriptParser#returnStatement.
    def exitReturnStatement(self, ctx:InterScriptParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by InterScriptParser#expressionStatement.
    def enterExpressionStatement(self, ctx:InterScriptParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by InterScriptParser#expressionStatement.
    def exitExpressionStatement(self, ctx:InterScriptParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by InterScriptParser#expression.
    def enterExpression(self, ctx:InterScriptParser.ExpressionContext):
        pass

    # Exit a parse tree produced by InterScriptParser#expression.
    def exitExpression(self, ctx:InterScriptParser.ExpressionContext):
        pass


    # Enter a parse tree produced by InterScriptParser#binaryOp.
    def enterBinaryOp(self, ctx:InterScriptParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by InterScriptParser#binaryOp.
    def exitBinaryOp(self, ctx:InterScriptParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by InterScriptParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:InterScriptParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by InterScriptParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:InterScriptParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by InterScriptParser#functionCall.
    def enterFunctionCall(self, ctx:InterScriptParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by InterScriptParser#functionCall.
    def exitFunctionCall(self, ctx:InterScriptParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by InterScriptParser#argumentList.
    def enterArgumentList(self, ctx:InterScriptParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by InterScriptParser#argumentList.
    def exitArgumentList(self, ctx:InterScriptParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by InterScriptParser#literal.
    def enterLiteral(self, ctx:InterScriptParser.LiteralContext):
        pass

    # Exit a parse tree produced by InterScriptParser#literal.
    def exitLiteral(self, ctx:InterScriptParser.LiteralContext):
        pass


    # Enter a parse tree produced by InterScriptParser#type.
    def enterType(self, ctx:InterScriptParser.TypeContext):
        pass

    # Exit a parse tree produced by InterScriptParser#type.
    def exitType(self, ctx:InterScriptParser.TypeContext):
        pass



del InterScriptParser