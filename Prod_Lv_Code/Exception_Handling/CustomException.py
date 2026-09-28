'''create your own custom exceptions by inheriting from Python's built-in Exception class. 
This makes your error reporting highly specific to your application domain.'''

# Defining a custom exception class
class InsufficientFundsError(Exception):
    """Raised when a user tries to withdraw more money than they have."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Attempted to withdraw ${amount} but balance is only ${balance}.")

# Using the custom exception
class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return f"Withdrew ${amount}. Remaining balance: ${self.balance}"

# --- Running the code ---
my_wallet = Wallet(100)

try:
    my_wallet.withdraw(250)
except InsufficientFundsError as e:
    print(f"Transaction Failed: {e}") 
    # Output: Transaction Failed: Attempted to withdraw $250 but balance is only $100.
