## super() is a built-in function used in the context of class inheritance. It returns a proxy object that allows you to refer to the parent or superclass, enabling access to its methods and attributes.

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1
    
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b = 3
    
obj = Employee()
print(obj.a)

obj = Programmer()
print(obj.a, obj.b)