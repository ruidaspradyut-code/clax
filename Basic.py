class Basic:
    @staticmethod
    def addition(a,b):
        return a+b
    
    @staticmethod
    def subtraction(a,b):
        return a-b
    
    @staticmethod
    def multiplication(a,b):
        return a*b
    
    @staticmethod
    def division(a,b):
        if b==0:
            print("Csn't be divided by zero!")
        else:
            return a/b

    @staticmethod    
    def percentage(self, a, b):
        return a * b / 100
    
