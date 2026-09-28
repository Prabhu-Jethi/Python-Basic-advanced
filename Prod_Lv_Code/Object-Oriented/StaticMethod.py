'''
Static methods behave exactly like isolated, regular functions, but they are housed inside a class namespace because they are logically
tied to the class topic.

• Behavior: Marked with the @staticmethod decorator, they take no mandatory first argument (self or cls). They cannot read or modify the object
or class state.
• Primary Use Case: Serving as a processing utility or validation helper that requires no persistent internal data.

'''

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    # Static method performing an isolated logic check
    @staticmethod
    def is_work_day(day_name):
        work_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
        return day_name.lower() in work_days

# --- Usage ---
# You do not need to instantiate the class to use a static method
print(Employee.is_work_day("Saturday"))  # Output: False
print(Employee.is_work_day("Monday"))    # Output: True
