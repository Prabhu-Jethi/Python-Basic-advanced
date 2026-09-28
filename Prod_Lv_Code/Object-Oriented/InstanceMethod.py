'''Instance methods are the standard, go-to methods in OOP. They are bound strictly to a specific object instance created from the class.

• The self parameter: The first argument is always self, which represents the specific object invoking the method. Through self, the method
can access and modify attributes distinct to that individual object.'''


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Instance variable
        self.balance = balance      # Instance variable

    # Instance method to modify object state
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount."

# --- Usage ---
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 50)

print(account1.deposit(500))  # Output: Deposited $500. New balance: $1500
print(account2.balance)       # Output: 50 (Bob's balance remains untouched)
