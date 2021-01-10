from lib.compileException import compileException
class ExpStmtNode():
    def __init__(self, stmt_type=None, expr=None ):
        self.stmt_type = stmt_type
        self.expr = expr

    def checkType(self, s):
        self.expr.checkType(s)
                    
    def text(self):
        print(f"Expr stmt:")
        self.expr.text()
        print(f"\n")
    def tryToFindRet(self, return_t, s, fun, fun_begin):
        return None