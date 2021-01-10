from lib.compileException import compileException
import math
class EBinNode():
    def __init__(self, exp_type=None, exprL=None, exprR=None, op=None, line=None ):
        self.exp_type = exp_type
        self.exprL = exprL
        self.exprR = exprR
        self.op=op
        self.line = line
        self.const = None
        self.type = None
        self.constL = exprL.get_const()
        self.constR = exprR.get_const()
        self.get_const()

    def checkType(self, s):
        # self.text()
        self.typeL = self.exprL.checkType(s)
        self.typeR = self.exprR.checkType(s)
        # print ( f"L = {self.typeL} R = {self.typeR}\n" )
        self.type = 'void'
        # print(f"OP = {self.op}\n")
        if self.typeL == "void":
             raise compileException(f"left side of {self.op} is void :C",self.line)
        
        if self.typeR == "void":
             raise compileException(f"right side of {self.op} is void :C",self.line)

        if self.typeL != self.typeR:
             raise compileException(f"mismach of types in ({self.op}) operator: left side: {self.typeL} right side: {self.typeR} :C",self.line)  

        if self.op in ['-', '*','/','%'] and self.typeL != "int":
           raise compileException(f"operator {self.op} cant be used with type {self.typeL} and {self.typeL} should be int :C",self.line)

        if self.op == '+' and ( self.typeL != 'int' and self.typeL != 'string' ):
            raise compileException(f"operator (+) cant be used with type {self.type} should be int/string :C",self.line)
        
        self.type = self.typeL
        return self.type 
    def get_const(self):
        if self.constL is None or self.constR is None:
            return None
        self.typeL = self.exprL.type
        self.typeR = self.exprR.type
        self.type = self.typeL 
        if self.typeL == "void":
             raise compileException(f"left side of {self.op} is void :C",self.line)
        
        if self.typeR == "void":
             raise compileException(f"right side of {self.op} is void :C",self.line)

        if self.typeL != self.typeR:
             raise compileException(f"mismach of types in ({self.op}) operator: left side: {self.typeL} right side: {self.typeR} :C",self.line)  

        if self.op in ['-', '*','/','%'] and self.typeL != "int":
           raise compileException(f"operator {self.op} cant be used with type {self.typeL} and {self.typeL} should be int :C",self.line)

        if self.op == '+' and ( self.typeL != 'int' and self.typeL != 'string' ):
            raise compileException(f"operator (+) cant be used with type {self.type} should be int/string :C",self.line)
        if self.op == '+':
            self.const = self.constL + self.constR
        if self.op == '-':
            self.const = self.constL - self.constR
        if self.op == '*':
            self.const = self.constL * self.constR

        if self.constR == 0:
           raise compileException(f"operator {self.op} division by 0 :C",self.line)
        if self.op == '/':
            self.const = self.constL // self.constR 
        if self.op == '%':
            self.const = self.constL % self.constR
            if self.constL < 0 and self.constR > 0:
                self.const = self.const - self.constR
        return self.const


    def text(self):
        print(f"EBinary exp: ")
        self.exprL.text()
        print(f"{self.op}")
        self.exprR.text()
        print(f" ")