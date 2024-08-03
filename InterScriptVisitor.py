from InterScriptParser import InterScriptParser
from InterScriptParserVisitor import InterScriptParserVisitor

class InterScriptVisitor(InterScriptParserVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}

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

        if func_name not in self.functions:
            raise Exception(f"Undefined function: {func_name}")

        params, body = self.functions[func_name]
        if len(args) != len(params):
            raise Exception(f"Function {func_name} expects {len(params)} arguments, got {len(args)}")

        # Save the current variable state and create a new one for the function call
        current_variables = self.variables.copy()
        self.variables = dict(zip(params, args))

        result = None
        for statement in body:
            result = self.visit(statement)
            if result is not None:  # Return statement
                break

        # Restore the original variable state
        self.variables = current_variables
        print(f"Function call: {func_name} with args {args} returned {result}")
        return result

    def visitIfStatement(self, ctx: InterScriptParser.IfStatementContext):
        # If statement handling
        print("Visiting If Statement")
        pass

    def visitForStatement(self, ctx: InterScriptParser.ForStatementContext):
        # For statement handling
        print("Visiting For Statement")
        pass

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
            print(f"Binary operation: {left} {operator} {right}")
            if operator == '+':
                left += right
            elif operator == '-':
                left -= right
            elif operator == '*':
                left *= right
            elif operator == '/':
                left /= right
            elif operator == '>':
                left = left > right
            elif operator == '<':
                left = left < right
            elif operator == '==':
                left = left == right
            elif operator == '!=':
                left = left != right
            else:
                raise Exception(f"Unknown operator: {operator}")
        return left

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
