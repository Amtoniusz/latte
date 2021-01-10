from lib.compileException import compileException
class EConstNode():
    def __init__(self, exp_type, type, val):
        self.exp_type = exp_type
        self.type = type
        self.val = val
        if (type == 'string'):
            self.const = val
        if (type == 'int'):
            self.const = int(val)
        if (val == 'true'):
            self.const = True
        if (val == 'false'):
            self.const = False


    def checkType(self, s):
        return self.type

    def get_const(self):
        return self.const

    def text(self):
        print(f"const exp: {self.exp_type} {self.type} {self.val} ")