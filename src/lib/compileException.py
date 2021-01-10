class compileException(Exception) :
    def __init__(self, message="sth went wrong :C", line=None):
        self.message = f"Error in line {line[0]} , column {line[1]} :{message}\n"
        super().__init__(self.message)