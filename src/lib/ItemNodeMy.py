from lib.compileException import compileException
class ItemNodeMy():
    def __init__(self, name=None, expr=None, line=None):
        self.name = name
        self.expr = expr
        self.line = line
        self.type = "ItemNodeMy bad type"

    #brak skutków ubocznych wywołąnia funkcji
    def checkType(self, s, type):
        # s.text()
        expr_type = type;
        if self.expr is not None:
            expr_type = self.expr.checkType(s)
        if  type != expr_type:
            raise compileException(f"mismach of types: declaredType = {type} expresion = {expr_type} :C",self.line)
        s.add(self.name, self)

            

    def text(self):
        if self.expr is not None:
            print(f"{self.name} <- ")
            self.expr.text()
            print(f", ")
        else:
            print(f"{self.name} <- None ")

    def tryToFindRet(self, return_t, s, fun, fun_begin):
        return None