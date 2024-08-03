import sys
import os
import requests
import zipfile
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

    def install_library(self, library_name):
        url = f"https://inter-script.github.io/library/{library_name}.zip"
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"{library_name}.zip", 'wb') as f:
                f.write(response.content)
            with zipfile.ZipFile(f"{library_name}.zip", 'r') as zip_ref:
                zip_ref.extractall("./libraries")
            os.remove(f"{library_name}.zip")
            print(f"Library {library_name} installed successfully.")
        else:
            print(f"Failed to download library {library_name}.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Main.py <source-file> | inter install <library> | help")
        sys.exit(1)

    command = sys.argv[1]

    if command == "help":
        print("Usage:")
        print("  python Main.py <source-file>    Compile and run a InterScript file.")
        print("  python Main.py inter install <library>    Install a library.")
        print("  python Main.py help    Show this help message.")
    elif command == "inter" and len(sys.argv) == 4 and sys.argv[2] == "install":
        library_name = sys.argv[3]
        compiler = InterScriptCompiler()
        compiler.install_library(library_name)
    else:
        input_stream = FileStream(sys.argv[1])
        compiler = InterScriptCompiler()
        compiler.compile(input_stream)
