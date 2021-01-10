from lib.compileException import compileException
class TopdefNode():
    def __init__(self, t=None, name=None, args=None, block=None, line=None):
        self.type = t
        self.name = name
        self.args = args
        self.block = block
        self.line = line

    def text(self):
        print(f"{self.type} {self.name} ")
        for i in self.args:
            i.text()
        print(f"\n")

    def addTopDef(self, s):
        types= []
        args_names = []
        for arg in self.args:
            if arg.name in args_names:
                raise compileException(f"Argument {arg.name} repeated :C",self.line)
            args_names.append(arg.name)
            if arg.type == 'void':
                raise compileException(f"Argument {arg.name} cant be void type :C",self.line)   
            types.append(arg.type)
        
        s.add_fun(self.name, types, self)


    def checkReturn(self, s):
        self.block.checkReturnFun(self.type, s, self.name, self.line)

    def addYourself(self, s):
        types= []
        args_names =[]
        for arg in self.args:
            s.add(arg.name, arg)
            if arg.type == 'void':
                raise compileException(f"Argument {arg.name} cant be void type :C",self.line)   
            types.append(arg.type)

    def checkType(self, s):
        self.addYourself(s)
        sCopy = s.dcopy()
        sCopy.clear_venv()
        self.block.checkType(s)
        return sCopy