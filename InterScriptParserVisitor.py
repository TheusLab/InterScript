# Generated from InterScriptParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .InterScriptParser import InterScriptParser
else:
    from InterScriptParser import InterScriptParser

# This class defines a complete generic visitor for a parse tree produced by InterScriptParser.

class InterScriptParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by InterScriptParser#program.
    def visitProgram(self, ctx:InterScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#statement.
    def visitStatement(self, ctx:InterScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:InterScriptParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:InterScriptParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#parameterList.
    def visitParameterList(self, ctx:InterScriptParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#parameter.
    def visitParameter(self, ctx:InterScriptParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#ifStatement.
    def visitIfStatement(self, ctx:InterScriptParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#forStatement.
    def visitForStatement(self, ctx:InterScriptParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#returnStatement.
    def visitReturnStatement(self, ctx:InterScriptParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx:InterScriptParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#expression.
    def visitExpression(self, ctx:InterScriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#binaryOp.
    def visitBinaryOp(self, ctx:InterScriptParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:InterScriptParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#functionCall.
    def visitFunctionCall(self, ctx:InterScriptParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#argumentList.
    def visitArgumentList(self, ctx:InterScriptParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#literal.
    def visitLiteral(self, ctx:InterScriptParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterScriptParser#type.
    def visitType(self, ctx:InterScriptParser.TypeContext):
        return self.visitChildren(ctx)



del InterScriptParser