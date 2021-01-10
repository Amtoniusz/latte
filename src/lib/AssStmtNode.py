from lib.compileException import compileException
class AssStmtNode():
    def __init__(self, stmt_type=None, name=None, expr=None, line=None ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.name = name
        self.line = line
        self.return_type = None

    #brak skutków ubocznych wywołąnia funkcji
    def checkType(self, s):
        # s.text()
        expr_type = self.expr.checkType(s)

        var = s.find(self.name);
        if var is None:
            raise compileException(f"Variable {self.name} not defined :C",self.line)  
        if  var.type != expr_type:
            raise compileException(f"mismach of types in assigment: varible type = {var.type} expresion = {expr_type} :C",self.line)
        

    def text(self):
        print(f"Ass stmt: {self.name} = ")
        self.expr.text()
        print(f"\n")

    def checkReturn(self,s,fun):
        return  self.return_type