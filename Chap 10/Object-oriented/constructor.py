## __init__ is the constructor in python.
## It is automatically called when you create a new object of the class.

class Employee:
    domain = "DA"
    salary = 40000
    
    def __init__(self, name, salary, domain): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.domain = domain
        print("Creating an object")
        
    def getInfo(self):
        print(f"Domain is {self.domain}. Salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good Morning...")
        
prabhu = Employee("prabhu", 50000, "Devops")
prabhu.greet()
print(prabhu.name, prabhu.salary, prabhu.domain)