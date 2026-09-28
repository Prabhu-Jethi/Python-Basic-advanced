## Dunder methods also known as Magic Methods
'''Operator overloading allows you to change how standard mathematical, comparison, or logical operators (like +, -, <, ==) 
behave when applied to your custom objects. This is achieved by overriding special Dunder (Double Underscore) methods.'''


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # Overloading the '==' operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overloading the print() output representation
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

# --- Usage ---
v1 = Vector2D(2, 4)
v2 = Vector2D(5, 3)
v3 = Vector2D(2, 4)

v_sum = v1 + v2  # Internally calls v1.__add__(v2)
print(v_sum)     # Output: Vector2D(7, 7)

print(v1 == v2)  # Output: False (Calls __eq__)
print(v1 == v3)  # Output: True


