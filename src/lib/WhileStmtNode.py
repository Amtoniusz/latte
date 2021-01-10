from lib.compileException import compileException
class WhileStmtNode():
    def __init__(self, stmt_type=None, expr=None, block=None, line=None ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.block = block
        self.line = line
        self.return_type = None


    def checkType(self, s):
        expr_type = self.expr.checkType(s)
        if expr_type not in ["int", "boolean"]:
            raise compileException(f"Condition must bo of type int/boolean cant be {expr_type} :C",self.line)
        self.block.checkType(s)
                
    def text(self):
        print(f"While stmt: ")
        self.expr.text()
        print(f" ")
        print(f"[{self.block.text()}]")


    def checkReturn(self,s,fun):
        # print(f"WHILE ->\n\n")
        self.return_type = self.block.checkReturn(s,fun)
        if self.return_type is not None:
            return self.return_type

        if self.expr.const  == True:
            self.return_type = "inf"
        
        return self.return_type

