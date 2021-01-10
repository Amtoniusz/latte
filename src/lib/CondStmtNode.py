from lib.compileException import compileException
class CondStmtNode():
    def __init__(self, stmt_type=None, expr=None, blockTrue=None,  blockFalse=None, line=None ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.blockTrue = blockTrue
        self.blockFalse = blockFalse
        self.line = line

    def checkType(self, s):
        expr_type = self.expr.checkType(s)
        if expr_type not in ["int", "boolean"]:
            raise compileException(f"Condition must bo of type int/boolean cant be {expr_type} :C",self.line)
        self.blockTrue.checkType(s)
        if self.stmt_type == "CondElse":
            self.blockFalse.checkType(s)
                
    def text(self):
        print(f"Cond stmt: ")
        self.expr.text()
        print(f" [")
        self.blockTrue.text()
        print(f"]") 
        if self.stmt_type == "CondElse":
            print(f" else [")
            self.blockFalse.text()
            print(f"]")


    def tryToFindRet(self, return_t, s, fun, fun_begin):
        retT = self.blockTrue.tryToFindRet( return_t, s, fun, fun_begin)
        if self.stmt_type == "Cond":
            return None
        retF = self.blockFalse.tryToFindRet( return_t, s, fun, fun_begin)
        if retT is None:
            return None
        if retF is None:
            return None
        return retT