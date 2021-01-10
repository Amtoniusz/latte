from lib.compileException import compileException
class RetStmtNode():
    def __init__(self, stmt_type=None, expr=None, line=None ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.line = line
        self.return_type = None

    def checkType(self, s):
        self.expr_type = "void"
        self.return_type ="void"
        if self.stmt_type == "Ret":
            self.expr_type = self.expr.checkType(s)
            self.return_type =self.expr_type
          
    def text(self):
        if self.stmt_type == "Ret":
            print(f"Ret stmt: ")
            self.expr.text()
            print(f"\n")
        else:
            print(f"VRet stmt\n")
    def checkReturn(self,s,fun):
        return self.return_type