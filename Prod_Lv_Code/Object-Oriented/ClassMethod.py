'''
Class methods are bound to the class itself, not to any single instance. They can modify the state of the class, which automatically
applies to all future instances of that class.

• The cls parameter: Marked with the @classmethod decorator, its first parameter is cls, pointing directly to the class definition.
• Primary Use Case: Frequently used to build factory methods that construct objects using alternative formats (e.g., parsing a string 
or JSON to create an object).

'''

class Book:
    total_books_created = 0  # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books_created += 1

    # Class method acting as an Alternative Constructor (Factory)
    @classmethod
    def from_string(cls, book_info_str):
        # Parses a string like "The Hobbit, J.R.R. Tolkien"
        title, author = book_info_str.split(", ")
        return cls(title, author)  # Returns a new instance: Book(title, author)

    # Class method to access class variables
    @classmethod
    def get_total_count(cls):
        return f"Total books cataloged: {cls.total_books_created}"

# --- Usage ---
# Creating an instance normally
b1 = Book("1984", "George Orwell")

# Creating an instance using the class method factory
b2 = Book.from_string("Dune, Frank Herbert")

print(b2.author)            # Output: Frank Herbert
print(Book.get_total_count()) # Output: Total books cataloged: 2
