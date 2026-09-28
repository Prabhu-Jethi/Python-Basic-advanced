'''
Polymorphism is a core pillar of Object-Oriented Programming (OOP) that means "many forms." In Python, 
it allows different classes to have methods with the exact same name but entirely different underlying logic.
'''

class File:
    def __init__(self, name):
        self.name = name

    def open(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Child class 1
class ImageFile(File):
    def open(self):
        return f"Rendering image canvas for {self.name}..."

# Child class 2
class TextFile(File):
    def open(self):
        return f"Opening text editor to read text from {self.name}..."

# --- Unified Interface Function ---
def execute_open(file_obj):
    # This single function handles any object that inherits from File
    print(file_obj.open())

# --- Usage ---
files = [ImageFile("photo.png"), TextFile("notes.txt")]

for file in files:
    execute_open(file)
    
# Output:
# Rendering image canvas for photo.png...
# Opening text editor to read text from notes.txt...




'''Without duck-typing'''

class CreditCard:
    def process_payment(self, amount):
        return f"Charging ${amount} to Credit Card via banking gateway."

class PayPal:
    def process_payment(self, amount):
        return f"Redirecting to PayPal gateway to authorize ${amount}."

# Unrelated class, but has the matching method
class Bitcoin:
    def process_payment(self, amount):
        return f"Verifying block transaction for {amount} BTC."

# --- Unified Payment Processor ---
def checkout(payment_method, total):
    # Python doesn't care about the class type, only that 'process_payment' exists
    print(payment_method.process_payment(total))

# --- Usage ---
card = CreditCard()
wallet = PayPal()
crypto = Bitcoin()

checkout(card, 150)   # Output: Charging $150 to Credit Card via banking gateway.
checkout(wallet, 150) # Output: Redirecting to PayPal gateway to authorize $150.
checkout(crypto, 0.05) # Output: Verifying block transaction for 0.05 BTC.
