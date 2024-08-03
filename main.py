import sys
from antlr4 import *
from InterScriptLexer import InterScriptLexer
from InterScriptParser import InterScriptParser
from InterScriptVisitor import InterScriptVisitor

class InterScriptCompiler:
    def compile(self, input_stream):
        lexer = InterScriptLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = InterScriptParser(stream)
        tree = parser.program()

        visitor = InterScriptVisitor()
        visitor.visit(tree)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <source-file>")
        sys.exit(1)

    input_stream = FileStream(sys.argv[1])
    compiler = InterScriptCompiler()
    compiler.compile(input_stream)
