from lib.compileException import compileException
class DeclStmtNode():
    def __init__(self, stmt_type=None, t=None, items=None, line=None ):
        self.stmt_type = stmt_type
        self.type = t
        self.items = items
        self.line = line
        for i in self.items:
            i.type = self.type

    def checkType(self, s):
        if self.type == 'void':
            raise compileException(f" Declaration cant be of void type :C",self.line)
        for i in self.items:
           i.checkType(s, self.type)
        return s 

    def text(self):
        print(f"decl stmt ({len(self.items)}) :")
        for i in self.items:
            i.text()
    def tryToFindRet(self, return_t, s, fun, fun_begin):
        return None