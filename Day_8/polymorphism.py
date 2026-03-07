# POLMORPHISM

# Using same method name or operation to peform two or more different operations
# Method Overloading
class Temp:
    def sum(self, a, b):
        print(a+b)
    # Mokey Patching :-
    # It is a method of storing the previous method's address inside a variable before overidding the method area's address. 
    # using that var we can access the previos method's methid ares
    add_to_sum = sum
    def sum(self, a, b, c):
        print(a+b+c)
obj = Temp()
obj.add_to_sum(10, 20)
# obj.sum(10, 20, 30)
# In pyhton, if we want ro perform mrthod overloading then it will act as method overriding.
# In other programming languages, based upon no. of arguments, the respective method block will get executed. But in pyhton it never happens



class MyDataType:
    def __init__(self, val):
        self.val = val
    def __add__(self, ano_obj):
        return self.val + ano_obj.val
    def __mul__(self, ano_obj):
        return self.val * ano_obj.val