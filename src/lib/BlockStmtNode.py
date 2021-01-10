from lib.compileException import compileException
class BlockStmtNode():
    def __init__(self, stmt_type=None ,stmts=None, line=None ):
        self.stmt_type = stmt_type
        self.stmts = stmts
        self.line = line
        self.return_type = None
        
    def checkType(self, s):
        sCopy = s.dcopy()
        s.new_block_declarations()
        for stmt in self.stmts:
            stmt.checkType(s)
            # stmt.text()
            # s.text()
        return sCopy

    def checkReturnMainFunctionBlock(self,s, fun):
        if len(self.stmts) == 0 and fun.return_type != 'void':
            raise compileException(f" {fun.return_type} {fun.name} without return :C",fun.line)
        type = self.checkReturn(s,fun)
        if type == 'inf':
            self.return_type = 'inf'
            return 'inf'
        if type is None and fun.return_type == 'void':
            self.return_type = 'void'
            return 'void'

        if type != fun.return_type:
            raise compileException(f" {fun.return_type} {fun.name} with return type of type {type} :C",fun.line)



        

    def checkReturn(self,s,fun):
        ret = []
        for stmt in self.stmts:
            stmt.checkReturn(s,fun)
            ret.append(stmt.return_type)
        # print(ret)
        ret = list(filter(lambda r: r is not None, ret))
        # print(ret)    
        ret_all = ret
        ret = list(filter(lambda r: r != 'inf', ret)) 
        ret = list(dict.fromkeys(ret))
        if len(ret) > 1:
            raise compileException(f" Function [{fun.return_type} {fun.name}] without return of 2or more types {ret[0]}{ret[1]}:C",self.line)
        if len(ret) == 1:
            if ret[0] != fun.return_type:
                raise compileException(f" Function [{fun.return_type} {fun.name}] without return type of  {ret[0]}:C",self.line)    

        if len(ret_all) == 0:
            return None
        self.return_type = ret_all[0]
        return self.return_type



    def text(self):
        print(f"BLOK(size:{len(self.stmts)}) ")
        for stmt in self.stmts:
            stmt.text()
