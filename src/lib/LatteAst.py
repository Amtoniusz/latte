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


class ArgNode():
    def __init__(self, t=None, name=None):
        self.type = t
        self.name = name