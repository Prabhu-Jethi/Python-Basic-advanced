## Create a class 'Programmer' for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
        
p = Programmer("P", 50000, "Analyst")
print(p.name, p.salary, p.role, p.company)
r = Programmer("R", 40000, "Developer")
print(r.name, r.salary, r.role, r.company)