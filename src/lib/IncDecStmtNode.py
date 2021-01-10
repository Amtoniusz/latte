from lib.compileException import compileException
class IncDecStmtNode():
    def __init__(self, stmt_type=None, name=None, line=None ):
        self.stmt_type = stmt_type
        self.name = name
        self.line =line
        self.return_type = None

    def checkType(self, s):
        type = s.find(self.name).type;
        if type is None:
            raise compileException(f"Variable {self.name} not defined :C",self.line)
        if type != "int" and self.stmt_type == "Inc":
            raise compileException(f"Variable {self.name} of type {type} cant be increded (++) :C",self.line)
        if type != "int" and self.stmt_type == "Dec":
            raise compileException(f"Variable {self.name} of type {type} cant be decreded (--) :C",self.line)    

    def text(self):
        if self.stmt_type == "Inc":
            print(f"IncDec stmt: {self.name}++\n")
        else:
            print(f"IncDec stmt: {self.name}--\n")

    def checkReturn(self,s,fun):
        return self.return_type