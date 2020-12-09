import copy
class State():
    def __init__(self, venv=None, fenv=None):
        self.venv = venv
        self.fenv = fenv

    def add (self, name, t ):
        self.venv[name]=t

    def add_fun (self, name, ts, t ):
        ts = str(ts)
        self.fenv[(name, ts)]=t

    def find (self, name):
        return self.fenv.get(name, default = None)

    def find_fun (self, name, ts):
        ts = str(ts)
        return self.venv.get((name,ts), default = None)

    def dcopy(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.venv = copy.deepcopy(self.venv)
        result.fenv = copy.deepcopy(self.fenv)
        return result

    def text (self):
        print(f"var: {self.venv}")
        print(f"fun: {self.fenv}\n")
