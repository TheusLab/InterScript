from InterScriptParser import InterScriptParser
from InterScriptParserVisitor import InterScriptParserVisitor

import subprocess
import websocket

class InterScriptVisitor(InterScriptParserVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.websockets = {}

    def visitProgram(self, ctx: InterScriptParser.ProgramContext):
        print("Visiting Program")
        for statement in ctx.statement():
            self.visit(statement)

    def visitVariableDeclaration(self, ctx: InterScriptParser.VariableDeclarationContext):
        var_name = ctx.IDENTIFIER().getText()
        var_value = self.visit(ctx.expression())
        self.variables[var_name] = var_value
        print(f"Variable declared: {var_name} = {var_value}")
        return var_value

    def visitFunctionDeclaration(self, ctx: InterScriptParser.FunctionDeclarationContext):
        func_name = ctx.IDENTIFIER().getText()
        params = [param.IDENTIFIER().getText() for param in ctx.parameterList().parameter()]
        body = ctx.statement()
        self.functions[func_name] = (params, body)
        print(f"Function declared: {func_name} with params {params}")
        return func_name

    def visitFunctionCall(self, ctx: InterScriptParser.FunctionCallContext):
        func_name = ctx.IDENTIFIER().getText()
        args = [self.visit(arg) for arg in ctx.argumentList().expression()]

        if func_name == "run_process":
            return self.run_process(args)

        if func_name == "connect_websocket":
            return self.connect_websocket(args)

        if func_name not in self.functions:
            raise Exception(f"Undefined function: {func_name}")

        params, body = self.functions[func_name]
        if len(args) != len(params):
            raise Exception(f"Function {func_name} expects {len(params)} arguments, got {len(args)}")

        current_variables = self.variables.copy()
        self.variables = dict(zip(params, args))

        result = None
        for statement in body:
            result = self.visit(statement)
            if result is not None:
                break

        self.variables = current_variables
        print(f"Function call: {func_name} with args {args} returned {result}")
        return result

    def run_process(self, args):
        command = args[0]
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        print(f"Process run: {command} with output: {result.stdout}")
        return result.stdout

    def connect_websocket(self, args):
        url = args[0]
        ws = websocket.WebSocket()
        ws.connect(url)
        self.websockets[url] = ws
        print(f"Connected to WebSocket: {url}")
        return f"Connected to {url}"

    def visitIfStatement(self, ctx: InterScriptParser.IfStatementContext):
        print("Visiting If Statement")
        condition = self.visit(ctx.expression())
        if condition:
            return self.visit(ctx.statement(0))
        elif ctx.ELSE():
            return self.visit(ctx.statement(1))

    def visitForStatement(self, ctx: InterScriptParser.ForStatementContext):
        print("Visiting For Statement")
        self.visit(ctx.variableDeclaration())
        while self.visit(ctx.expression()):
            self.visit(ctx.statement())
            self.visit(ctx.expressionStatement())

    def visitReturnStatement(self, ctx: InterScriptParser.ReturnStatementContext):
        print("Visiting Return Statement")
        return self.visit(ctx.expression())

    def visitExpressionStatement(self, ctx: InterScriptParser.ExpressionStatementContext):
        print("Visiting Expression Statement")
        return self.visit(ctx.expression())

    def visitExpression(self, ctx: InterScriptParser.ExpressionContext):
        print("Visiting Expression")
        left = self.visit(ctx.primaryExpr(0))
        for i in range(1, len(ctx.primaryExpr())):
            operator = ctx.binaryOp(i-1).getText()
            right = self.visit(ctx.primaryExpr(i))
            left = self.applyOperator(left, operator, right)
        return left

    def applyOperator(self, left, operator, right):
        print(f"Binary operation: {left} {operator} {right}")
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == '>':
            return left > right
        elif operator == '<':
            return left < right
        elif operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        else:
            raise Exception(f"Unknown operator: {operator}")

    def visitLiteral(self, ctx: InterScriptParser.LiteralContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.STRING():
            return str(ctx.STRING().getText().strip('"'))
        elif ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False

    def visitPrimaryExpr(self, ctx: InterScriptParser.PrimaryExprContext):
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name in self.variables:
                print(f"Accessing variable: {var_name} = {self.variables[var_name]}")
                return self.variables[var_name]
            else:
                raise Exception(f"Undefined variable: {var_name}")
        else:
            return self.visitChildren(ctx)
