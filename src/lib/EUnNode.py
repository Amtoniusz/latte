from lib.compileException import compileException
class EUnNode():
    def __init__(self, exp_type, expr, op, line):
        self.exp_type = exp_type
        self.expr = expr
        self.op=op
        self.line=line
        self.const = None
        self.type = None
        self.get_const()
    
    def checkType(self, s):
        self.type = self.expr.checkType(s)
        # print(f"OP = {self.op}\n")
        if self.op == '-' and self.type != 'int':
           raise compileException(f"operator (-) cant be used with type {self.type} should be int :C",self.line) 
        if self.op == '!' and self.type != 'boolean':
            raise compileException(f"operator (!) cant be used with type {self.type} should be boolean :C",self.line)
        return self.type

    def get_const(self):
        expr_const = self.expr.get_const()
        if expr_const is None:
            return None
        self.type = self.expr.type
        if self.op == '-':
            if self.type != 'int':
                raise compileException(f"operator (-) cant be used with type {self.type} should be int :C",self.line)
            else:
                self.const = -expr_const

        if self.op == '!':
            if self.type != 'boolean':
                raise compileException(f"operator (!) cant be used with type {self.type} should be boolean :C",self.line)
            else:
                self.const = not expr_const
        return self.const
        
    def text(self):
        print(f"EUnary exp: {self.op}")
        self.expr.text()
        print(f" ")
