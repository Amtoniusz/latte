import sys
import os
from antlr4 import *
from lib import *
from lib.State import State
from lib.TopdefNode import TopdefNode
from lib.LatteLexer import LatteLexer
from lib.LatteParser import LatteParser
from lib.LatteVisitor import LatteVisitor
debug = False
def checkType(topDefs, s):
    for topDef in topDefs:
        s = topDef.checkType(s)

# FUN  = TopdefNode('void')
FUN_printInt = TopdefNode ('void',"printInt",['int'],None, (0,0))
FUN_printString = TopdefNode ('void',"printString",['string'],None, (0,0))
FUN_readInt = TopdefNode ('int',"readInt",[],None, (0,0))
FUN_readString = TopdefNode ('string',"readString",[],None, (0,0))
def addTopdef(topDefs, s):
    s.add_fun ("printInt", ['int'], FUN_printInt)
    s.add_fun ("printString", ['string'],  FUN_printString)
    s.add_fun ("readInt", [], FUN_readInt)
    s.add_fun ("readString", [],  FUN_readString)
    for topDef in topDefs:
        topDef.addTopDef(s)

def checkRet(topDefs, s):
    for topDef in topDefs:
        topDef.checkReturn(s)


def compile (dir, path_in):
    with open(path_in, 'r') as f:
        text = InputStream(f.read())
        lexer = LatteLexer(text)
        stream = CommonTokenStream(lexer)
        parser = LatteParser(stream)
        tree = parser.program()

        if parser.getNumberOfSyntaxErrors() == 0:
            try:
                topDefs = LatteVisitor().visitProgram(tree)
                s = State({},{})
                addTopdef(topDefs, s)
                checkType(topDefs, s)
                checkRet(topDefs, s)
            except Exception as e:
                sys.stderr.write("ERROR\n")
                sys.stderr.write( f"exception: {e.message}" )
                sys.exit('1')

            sys.stderr.write("OK\n")
            sys.exit('0')
        else:
            sys.stderr.write("ERROR\n")
            sys.exit('1')


def main(argv):
    for path in argv[1:]:
        file = path
        dir = os.path.dirname(file)
        # print(f"dir  = {dir}\nfile = {file}\n") 
        compile (dir, file)
    

if __name__ == '__main__':    
    main(sys.argv)