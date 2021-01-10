from lib.compileException import compileException
#exp_type = EId
class EIdNode():
    def __init__(self, exp_type,name, line):
        self.exp_type = exp_type
        self.name = name
        self.line = line
        self.const = None
        self.type = None

    def checkType(self, s):
        # print ( f" {self.name} -> {s.find(self.name)} \n" )
        self.type = s.find(self.name).type
        if self.type is None:
            raise compileException(f"Variable {self.name} not defined :C",self.line)
        return self.type


    def text(self):
        print(f"EId expr: {self.name} ")
        
    def get_const(self):
        return self.const