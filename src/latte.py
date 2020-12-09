import sys
import os
from antlr4 import *
from lib import *
from lib.State import *
from lib.LatteAst import *
from lib.LatteLexer import LatteLexer
from lib.LatteParser import LatteParser
from lib.LatteVisitor import LatteVisitor
debug = False


def compile (dir, path_in):
    with open(path_in, 'r') as f:
        text = InputStream(f.read())
        lexer = LatteLexer(text)
        stream = CommonTokenStream(lexer)
        parser = LatteParser(stream)
        tree = parser.program()

        if parser.getNumberOfSyntaxErrors() == 0:
            try:
                LatteVisitor().visitProgram(tree)
            except compileException as e:
                print( f"exception: {e.message}" )

            print("STH")
        else:
            sys.exit('parser error')


def main(argv):
    for path in argv[1:]:
        file = path
        dir = os.path.dirname(file)
        print(f"dir  = {dir}\nfile = {file}\n") 
        compile (dir, file)
    

if __name__ == '__main__':    
    main(sys.argv)