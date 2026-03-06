class Book:
    # 1. Define Static Attributes here
    total_books = 0
    library_name = "New York Library"

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        # Increment the total count of books here
        Book.total_books += 1

    # 2. Define the Normal Method (Instance)
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return f"You have borrowed {self.title}."
        return f"Sorry, {self.title} is already out."

    # 3. Define the Class Method
    @classmethod
    def update_library(cls, new_name):
        # Your logic here
        cls.library_name = new_name

    # 4. Define the Static Method
    @staticmethod
    def validate_isbn(isbn_str):
        # Return True if length is 13 and it's all digits
        if len(isbn_str) == 13 and isbn_str.isdigit():
            return True
        return False

# --- TEST YOUR CODE ---
print(Book.validate_isbn("1234567890123")) # Should be True
b1 = Book("Python OOP", "Dr. Angela Yu")
print(b1.borrow_book())


b2 = Book("Python OOP-2", "Dr. Angela Yu")
print(b2.borrow_book())


b3 = Book("Python OOP-3", "Dr. Angela Yu")
print(b3.borrow_book())


print(Book.total_books)