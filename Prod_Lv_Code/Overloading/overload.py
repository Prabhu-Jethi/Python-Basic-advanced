'''

Feature	               |     Method Overriding	                               |      Method Overloading
-------------------------------------------------------------------------------------------------------------------------------------------
1. Definition	       |     A child class completely replaces or extends      |      A single class defines a method that can accept 
                       |     a method inherited from a parent class.	       |      different numbers or types of inputs.
                       |                                                       |
2. Classes Involved	   |    Requires at least two classes(Parent and Child).   |    Happens within a single class.
                       |                                                       |
3. Python Suport	   |    Fully supported natively.	                       |    Not natively supported by name alone 
                       |                                                       |    (the last defined method overwrites previous ones).
                       |                                                       |
4. Python Workaround   |    Uses standard inheritance and super().	           |    Uses default arguments or the @singledispatch decorator.


'''

### Overriding ###
class Animal:
    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    # Overriding the parent method completely
    def make_sound(self):
        return "Woof!"

class SubWoofer(Dog):
    # Extending the parent method using super()
    def make_sound(self):
        return super().make_sound() + " LOUD BARK!"

# --- Usage ---
print(Animal().make_sound())    # Output: Generic animal sound
print(Dog().make_sound())       # Output: Woof!
print(SubWoofer().make_sound())  # Output: Woof! LOUD BARK!



### Overloading ###

## Default overloading
class Calculator:
    # Simulating overloading by making parameters optional
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))     # Output: 15 (Acts like 2-argument method)
print(calc.add(5, 10, 20)) # Output: 35 (Acts like 3-argument method)


# type overloading ----
from functools import singledispatch

@singledispatch
def render(value):
    raise NotImplementedError(f"No renderer for {type(value)}")

@render.register
def _(value: int):
    return f"Integer: {value}"

@render.register
def _(value: str):
    return f"String: {value}"

render(5)      # "Integer: 5"
render("hi")   # "String: hi"

