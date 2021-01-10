from lib.compileException import compileException
class BlockStmtNode():
    def __init__(self, stmt_type=None ,stmts=None, line=None ):
        self.stmt_type = stmt_type
        self.stmts = stmts
        self.line = line
        
    def checkType(self, s):
        sCopy = s.dcopy()
        for stmt in self.stmts:
            stmt.checkType(s)
            # stmt.text()
            # s.text()
        return sCopy

    def checkReturnFun(self, return_t, s, fun, fun_begin):
        if len(self.stmts) == 0 and return_t != 'void':
            raise compileException(f" {return_t} {fun} without return :C",fun_begin)
        
        for i in  range(len(self.stmts)):
            stmt = self.stmts[i]
            t = stmt.stmt_type
            if t == "Ret" or t == "VRet":
                if return_t != stmt.expr_type:
                    raise compileException(f" {return_t} {fun} with return statment of type: {stmt.expr_type} :C",fun_begin)
                else:
                    if i != len(self.stmts)-1:
                        raise compileException(f" {return_t} {fun} with unrechable code :C",fun_begin)
                    else:
                        return

            if t == "CondElse" or t == "Cond":
                returned = stmt.tryToFindRet(return_t, s, fun, fun_begin)
                if returned == return_t:
                    return
        if return_t != 'void':
            raise compileException(f" Function [{return_t} {fun}] without return :C",fun_begin)
    



    def tryToFindRet(self, return_t, s, fun, fun_begin):
        for i in  range(len(self.stmts)):
            stmt = self.stmts[i]
            t = stmt.stmt_type
            
            if t == "Ret" or t == "VRet":
                if return_t != stmt.expr_type:
                    raise compileException(f" {return_t} {fun} with return statment of type: {stmt.expr_type} :C",fun_begin)
                else:
                    return return_t
            if t == "CondElse":
                return stmt.tryToFindRet(return_t, s, fun, fun_begin)
        return None

    def text(self):
        print(f"BLOK(size:{len(self.stmts)}) ")
        for stmt in self.stmts:
            stmt.text()
