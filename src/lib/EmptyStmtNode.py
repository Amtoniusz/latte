from lib.compileException import compileException
class EmptyStmtNode():
    def __init__(self, stmt_type=None ):
        self.stmt_type = stmt_type

    def checkType(self, s):
        pass

    def text(self):
        print(f"empty stmt")
        
    def tryToFindRet(self, return_t, s, fun, fun_begin):
        return None