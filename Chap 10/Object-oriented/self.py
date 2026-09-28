## Self represents the instance of the class (the object being created.
## It allows each object to have its own copy of the variables.

class Employee:
    domain = "Data Analytics" #class
    salary = 40000
    
    def getInfo(self):
        print(f"The domain is {self.domain}. The salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good Morning.")
        
prabhu = Employee()
prabhu.salary = 50000 #instance
prabhu.greet()
prabhu.getInfo()
# Employee.getInfo(prabhu)