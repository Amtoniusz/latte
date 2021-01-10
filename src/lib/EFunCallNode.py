from lib.compileException import compileException
class EFunCallNode():
    def __init__(self, exp_type=None, name=None ,exprs=None, line=None):
        self.exp_type = exp_type
        self.name = name
        self.type = None
        self.const = None
        self.exprs = exprs
        self.line = line

    def checkType(self, s):
        args_type = []
        for expr in self.exprs:
            expr_type = expr.checkType(s)
            args_type.append(expr_type)
        self.type = s.find_fun(self.name,args_type).type
        if self.type is None:
            raise compileException(f"function {self.name} with arguments of types: {args_type} wasnt declared :C",self.line)
        return self.type

    def text(self):
        print(f"Efun exp: {self.name}")
        for arg in self.exprs:
            arg.text()
        print(f" ") 

    def get_const(self):
        return self.const
