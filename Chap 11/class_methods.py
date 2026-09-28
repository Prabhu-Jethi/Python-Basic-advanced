class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
        
emp = Employee()

emp.a = 40

# print(emp.a)

emp.show()