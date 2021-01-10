from lib.compileException import compileException
class EmptyStmtNode():
    def __init__(self, stmt_type, line ):
        self.stmt_type = stmt_type
        self.return_type = None
        self.line = line

    def checkType(self, s):
        pass

    def text(self):
        print(f"empty stmt")
        
    def checkReturn(self,s,fun):
        return self.return_type