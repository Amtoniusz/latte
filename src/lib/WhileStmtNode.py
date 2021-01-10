from lib.compileException import compileException
class WhileStmtNode():
    def __init__(self, stmt_type=None, expr=None, stmt=None, line=None ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.stmt = stmt
        self.line = line


    def checkType(self, s):
        expr_type = self.expr.checkType(s)
        if expr_type not in ["int", "boolean"]:
            raise compileException(f"Condition must bo of type int/boolean cant be {expr_type} :C",self.line)
        self.stmt.checkType(s)
                
    def text(self):
        print(f"While stmt: ")
        self.expr.text()
        print(f" ")
        print(f"[{self.stmt.text()}]")

    def tryToFindRet(self, return_t, s, fun, fun_begin):
        return None