from lib.compileException import compileException
class RetStmtNode():
    def __init__(self, stmt_type=None, expr=None, line=None ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.line = line

    def checkType(self, s):
        self.expr_type = "void"
        if self.stmt_type == "Ret":
            self.expr_type = self.expr.checkType(s)
          
    def text(self):
        if self.stmt_type == "Ret":
            print(f"Ret stmt: ")
            self.expr.text()
            print(f"\n")
        else:
            print(f"VRet stmt\n")
    def tryToFindRet(self, return_t, s, fun, fun_begin):
        if self.expr_type != return_t:
            raise compileException(f" {return_t} {fun} with return statment of type: {self.expr_type} :C",fun_begin)
        else:
            return return_t