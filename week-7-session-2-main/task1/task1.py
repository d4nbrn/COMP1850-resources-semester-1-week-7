class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"This book is called {self.title}, it is written by {self.author} and published in {self.year}"
    def __repr__(self):
        return f"Book: Title = {self.title} Author = {self.author} Year = {self.year}"

newBook = Book("Harry potter","JK Rowling",1995)
print(newBook)
representation = newBook.__repr__()
print(representation)
# Given a Book class with the __init__ method, define the following special methods:
# (1) __str__ method - feel free to suggest a suitable string representation
# (2) __repr__ method - what do you think should be the format?
