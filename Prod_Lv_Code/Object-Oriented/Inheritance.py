'''
Inheritance allows a child class to inherit methods and attributes from a parent class. The child class can either use the parent's methods as-is, 
completely replace them (Method Overriding), or extend them using the super() function.

'''

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        # Calls the parent constructor to initialize name and base_salary
        super().__init__(name, base_salary)
        self.bonus = bonus

    # Overriding the parent's calculate_pay method
    def calculate_pay(self):
        # Uses super() to fetch base salary and adds the bonus
        return super().calculate_pay() + self.bonus

# --- Usage ---
emp = Employee("John", 4000)
mgr = Manager("Sarah", 6000, 1500)

print(f"{emp.name} Pay: ${emp.calculate_pay()}")  # Output: John Pay: $4000
print(f"{mgr.name} Pay: ${mgr.calculate_pay()}")  # Output: Sarah Pay: $7500
