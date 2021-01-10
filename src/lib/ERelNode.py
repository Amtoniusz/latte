from lib.compileException import compileException
class ERelNode():
    def __init__(self, exp_type=None, exprL=None, exprR=None, op=None, line=None):
        self.exp_type = exp_type
        self.exprL = exprL
        self.exprR = exprR
        self.op=op
        self.line=line
        self.constL = exprL.get_const()
        self.constR = exprR.get_const()
        self.type=None
        self.const=None
        self.get_const()
        self.type = 'boolean'


    def checkType(self, s):
        self.typeL = self.exprL.checkType(s)
        self.typeR = self.exprR.checkType(s)
        # print(f"OP = {self.op}\n")
        if self.typeL == "void":
             raise compileException(f"left side of {self.op} is void :C",self.line)
        
        if self.typeR == "void":
             raise compileException(f"right side of {self.op} is void :C",self.line)

        if self.typeL != self.typeR and (self.typeL == 'string' or self.typeR == 'string'):
             raise compileException(f"mismach of types in ({self.op}) operator: left side: {self.typeL} right side: {self.typeR} :C",self.line)  
        
        self.type = 'boolean'

        return self.type   
    def get_const(self):
        if self.constL  is None or self.constR is None:
            return None
        self.typeL = self.exprL.type
        self.typeR = self.exprR.type

        if self.typeL == "void":
             raise compileException(f"left side of {self.op} is void :C",self.line)
        
        if self.typeR == "void":
             raise compileException(f"right side of {self.op} is void :C",self.line)

        if self.typeL != self.typeR and (self.typeL == 'string' or self.typeR == 'string'):
             raise compileException(f"mismach of types in ({self.op}) operator: left side: {self.typeL} right side: {self.typeR} :C",self.line)

        if self.typeL != self.typeR and (self.typeL == 'string' or self.typeR == 'string'):
             raise compileException(f"mismach of types in ({self.op}) operator: left side: {self.typeL} right side: {self.typeR} :C",self.line)  

        if self.op == '<':
            self.const = self.constL < self.constR
        if self.op == '<=':
            self.const = self.constL <= self.constR
        if self.op == '>':
            self.const = self.constL > self.constR
        if self.op == '>=':
            self.const = self.constL >= self.constR
        if self.op == '==':
            self.const = self.constL == self.constR
        if self.op == '!=':
            self.const = self.constL != self.constR
        return self.const
      

            
    def text(self):
        print(f"ERel exp: ")
        self.exprL.text()
        print(f"{self.op}")
        self.exprR.text()
        print(f" ")
