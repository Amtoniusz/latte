from lib.compileException import compileException
class EAndNode():
    def __init__(self, exp_type=None, exprL=None, exprR=None, op=None, line=None ):
        self.exp_type = exp_type
        self.exprL = exprL
        self.exprR = exprR
        self.op=op
        self.line =line 
        self.type=None
        self.const=None
        self.type = 'boolean'
        self.get_const()

    def checkType(self, s):
        self.typeL = self.exprL.checkType(s)
        self.typeR = self.exprR.checkType(s)
        # print(f"OP = {self.op}\n")
        if self.typeL not in ["boolean", "int"]:
            raise compileException(f"left side of {self.op} is not boolean/int :C",self.line)
        
        if self.typeR not in ["boolean", "int"]:
            raise compileException(f"right side of {self.op} is not boolean/int :C",self.line) 

        return self.type 

    def text(self):
        print(f"EAndOr exp: ")
        self.exprL.text()
        print(f"{self.op}")
        self.exprR.text()
        print(f" ")

    def get_const(self):
        self.constL = self.exprL.get_const()
        if self.constL is None:
            return None
        self.typeL = self.exprL.type

        if self.typeL not in ["boolean", "int"]:
            raise compileException(f"left side of {self.op} is not boolean/int :C",self.line)
        
        cL = self.constL
        if (self.exprL.type == "int"):
            cL = self.constL != 0
        if cL  == False:
            return False

        self.constR = self.exprR.get_const()
        if self.constR is None:
            return None
        self.typeR = self.exprR.type
        
        if self.typeR not in ["boolean", "int"]:
            raise compileException(f"right side of {self.op} is not boolean/int :C",self.line)
        
        
        cR = self.constR
        if (self.exprR.type == "int"):
            cR = self.constR != 0   

        self.const = cR and cL 
        return self.const

class EOrNode():
    def __init__(self, exp_type=None, exprL=None, exprR=None, op=None, line=None ):
        self.exp_type = exp_type
        self.exprL = exprL
        self.exprR = exprR
        self.op=op
        self.line =line 
        self.type=None

    def checkType(self, s):
        self.typeL = self.exprL.checkType(s)
        self.typeR = self.exprR.checkType(s)
        # print(f"OP = {self.op}\n")
        if self.typeL not in ["boolean", "int"]:
            raise compileException(f"left side of {self.op} is not boolean/int :C",self.line)
        
        if self.typeR not in ["boolean", "int"]:
            raise compileException(f"right side of {self.op} is not boolean/int :C",self.line) 
        
        self.type = 'boolean'

        return self.type 

    def text(self):
        print(f"EAndOr exp: ")
        self.exprL.text()
        print(f"{self.op}")
        self.exprR.text()
        print(f" ")

    def get_const():
        self.constL = self.exprL.get_const()
        if self.constL is None:
            return None
        self.typeL = self.exprL.type

        if self.typeL not in ["boolean", "int"]:
            raise compileException(f"left side of {self.op} is not boolean/int :C",self.line)
        
        cL = self.constL
        if (self.exprL.type == "int"):
            cL = self.constL != 0
        if cL  == True:
            return True

        self.constR = self.exprR.get_const()
        if self.constR is None:
            return None
        self.typeR = self.exprR.type
        
        if self.typeR not in ["boolean", "int"]:
            raise compileException(f"right side of {self.op} is not boolean/int :C",self.line)
        
        
        cR = self.constR
        if (self.exprR.type == "int"):
            cR = self.constR != 0 

        self.const = cR or cL 
        return self.const

