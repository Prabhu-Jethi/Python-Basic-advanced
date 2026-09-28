class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
        
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
emp = Employee()
emp.a = 45

emp.name = "Prabhu Jethi"
print(emp.fname, emp.lname)

# emp.show()