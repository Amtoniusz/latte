from lib.compileException import compileException
class ExpStmtNode():
    def __init__(self, stmt_type, expr, line ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.return_type = None
        self.line = line

    def checkType(self, s):
        self.expr.checkType(s)
                    
    def text(self):
        print(f"Expr stmt:")
        self.expr.text()
        print(f"\n")

    def checkReturn(self,s,fun):
        return self.return_type