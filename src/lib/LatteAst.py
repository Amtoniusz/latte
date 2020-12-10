from .State import *
class compileException(Exception):
    def __init__(self, message="sth went wrong :C" ):
        self.message = message
        super().__init__(self.message)


class TopdefNode():
    def __init__(self, t=None, name=None, args=None, block=None):
        self.type = t
        self.name = name
        self.args = args
        self.block = block

    def text(self):
        print(f"{self.type} {name} ")
        for i in args:
            i.text()
        print(f"\n")


class ArgNode():
    def __init__(self, t=None, name=None):
        self.type = t
        self.name = name


class BlockStmtNode():
    def __init__(self, stmt_type=None ,stmts=None ):
        self.stmt_type = stmt_type
        self.stmts = stmts
        

    def text(self):
        print(f"BLOK(size:{len(self.stmts)}) ")
        for stmt in self.stmts:
            stmt.text()


class EmptyStmtNode():
    def __init__(self, stmt_type=None ):
        self.stmt_type = stmt_type

    def text(self):
        print(f"empty stmt")

class EmptyStmtNode():
    def __init__(self, stmt_type=None ):
        self.stmt_type = stmt_type

    def text(self):
        print(f"empty stmt")

class DeclStmtNode():
    def __init__(self, stmt_type=None, t=None, items=None ):
        self.stmt_type = stmt_type
        self.type = t
        self.items = items

    def text(self):
        print(f"decl stmt ({len(self.items)}) :")
        for i in self.items:
            i.text()

class ItemNodeMy():
    def __init__(self, name=None, expr=None):
        self.name = name
        self.expr = expr


    def text(self):
        if self.expr is not None:
            print(f"{self.name} <- {self.expr} ")
        else:
            print(f"{self.name} <- TODO ")

class AssStmtNode():
    def __init__(self, stmt_type=None, name=None, expr=None ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.name = name

    def text(self):
        print(f"Ass stmt: {self.name} = {self.expr}\n")

class IncDecStmtNode():
    def __init__(self, stmt_type=None, name=None ):
        self.stmt_type = stmt_type
        self.name = name

    def text(self):
        if self.stmt_type == "Inc":
            print(f"IncDec stmt: {self.name}++\n")
        else:
            print(f"IncDec stmt: {self.name}--\n")

class RetStmtNode():
    def __init__(self, stmt_type=None, expr=None ):
        self.stmt_type = stmt_type
        self.expr = expr

    #TODO
    def text(self):
        if self.stmt_type == "VRet":
            print(f"VRet stmt: {self.expr}++\n")
        else:
            print(f"Ret stmt\n")


class CondStmtNode():
    def __init__(self, stmt_type=None, expr=None, blockTrue=None,  blockFalse=None ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.blockTrue = blockTrue
        self.blockFalse = blockFalse

    #TODO
    def text(self):
        print(f"Cond stmt: {self.expr}")
        print(f"[")
        self.blockTrue.text()
        print(f"]") 
        if self.stmt_type == "CondElse":
            print(f" else [")
            self.blockFalse.text()
            print(f"]")



class WhileStmtNode():
    def __init__(self, stmt_type=None, expr=None, stmt=None ):
        self.stmt_type = stmt_type
        self.expr = expr
        self.stmt= stmt


    #TODO
    def text(self):
        print(f"While stmt: {self.expr}\n")
        print(f"[{self.stmt.text()}]") 


class ExpStmtNode():
    def __init__(self, stmt_type=None, expr=None,  ):
        self.stmt_type = stmt_type
        self.expr = expr
       

    #TODO
    def text(self):
        print(f"Expr stmt: {self.expr}\n")
        # print(f"[{self.stmt.text()}]") 