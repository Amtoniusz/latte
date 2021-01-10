from lib.compileException import compileException
class CondStmtNode():
    def __init__(self, stmt_type=None, expr=None, blockTrue=None,  blockFalse=None, line=None ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.blockTrue = blockTrue
        self.blockFalse = blockFalse
        self.line = line
        self.return_type = None

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


    def checkReturn(self,s,fun):
        bTret = self.blockTrue.checkReturn(s,fun)
        bFret = None
        if self.blockFalse is not None:
            bFret =self.blockFalse.checkReturn(s,fun)
        # print(f"True bloak type = {bTret}\n")
        # print(f"False bloak type = {bFret}\n")
        if self.expr.const is not None and self.expr.const == True:
            self.return_type = bTret
            return bTret
        if self.expr.const is not None and self.expr.const == False:
            self.return_type = bFret
            return bFret
        if bFret is None or bTret is None:
            self.return_type = None
            return None
        
        if bFret  == 'inf' :
            self.return_type = bTret
            return self.return_type
        if bTret  == 'inf' :
            self.return_type = bFret
            return self.return_type
        if bTret != bFret:
            raise compileException(f"Wrong return type in function {fun.name}: {bFret} or {bTret} :C",self.line)
            
        self.return_type = bTret
        return self.return_type


