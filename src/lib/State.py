import copy
from lib.compileException import compileException
    

class State():
    #venv variable envirement variable name -> (declared in this block, )
    def __init__(self, venv=None, fenv=None, arrenv=None):
        self.venv = venv
        self.fenv = fenv
        self.arrenv = arrenv 
        self.return_type = None

    def add (self, name, var):
        v = self.f(name)
        
        if v is not None and v[0] == True:
            raise compileException(f"Variable {name} was defined here:  {v[1].line} " ,  var.line)
        self.venv[name]=(True,var)

    def add_fun (self, name, ts, fun):
        ts = str(ts)
        line = fun.line
        if self.find_fun(name, ts) is not None:
            raise compileException(f"Function {name} was defined here: in line {self.find_fun_loc(name, ts)} " , line)
        self.fenv[(name, ts)]=(True,fun)

    def f (self, name):
        return self.venv.get(name, None)

    def find (self, name):
        var = self.f(name)
        if var is not None:
            return var[1]
        return None
    
    def definde_in_this_block(name):
        var = self.f(name)
        if var is not None:
            return var[0]
        return False

    def find_loc (self, name):
        return self.find(name).line

    def f_fun(self, name, ts):
        ts = str(ts)
        fun = (self.fenv).get((name,ts), None)
        return fun

    def find_fun (self, name, ts):
        ts = str(ts)
        fun = self.f_fun(name, ts)
        if fun is not None:
            return fun[1]
        return None

    def find_fun_loc (self, name, ts):
        return self.find_fun(name,ts).line

    def dcopy(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.venv = copy.deepcopy(self.venv)
        result.fenv = copy.deepcopy(self.fenv)
        return result

    def new_block_declarations(self):
        for k,(_,v) in self.venv.items():
            self.venv[k] = (False,v)
        for k,(_,v) in self.fenv.items():
            self.venv[k] = (False,v)

    def clear_venv(self):
        self.venv.clear()

    def text (self):
        print(f"var:\n")
        for k in self.venv.keys():
            v = self.venv[k]
            print(f"{k} -> {v}\n")
        print(f"\nfun:\n")
        for k in self.fenv.keys():
            v = self.fenv[k]
            print(f"{k} -> {v}")
        print(f"\n\n")

