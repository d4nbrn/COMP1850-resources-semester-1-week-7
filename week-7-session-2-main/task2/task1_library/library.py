from book import Book
# Define a Library class with the following fields:
# (1) name - the name of a library, e.g., Laidlaw Library
# (2) books - a list of Book instances
# When an instance of Library is created, only the name field is required for the __init__ method.

class Library():
    def __init__(self,name):
        self.name = name
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def __str__(self):
        string = f"Library: {self.name} \nBooks:"
        for book in self.books:
            string = string + book.__str__() +"\n"
        return string

# The Library class also has the following methods:
# (1) add_book(book) - adds a Book instance to the library, i.e., add the Book instance to the books field
# (2) __str__ - returning the library name and list of books titles in the format 
# Library: City Library\nBooks:\n- To Kill a Mockingbird by Harper Lee (1960)\n- 1984 by George Orwell (1949)

# When complete, create 3 instances of Books for your 3 most favourite books
# Then, create an instance of Library with your most favourite library in Leeds University
# and add the 3 books to the library. Then, print the library you have created using the print method
HarrPotterAndThePhilosophersStone = Book("Harry Potter and the Philosophers Stone","JK Rowling",1995,"1st")
DiaryOfAWimpyKid = Book("Diary of a wimpy Kid","Jeff Kinny", 2007, "1st")
HitchhikersGuide = Book("Hitchhikers Guide to the Galaxy", "Some Fella", 1960, "3rd")

library = Library("Laidlaw Library")
library.add_book(HarrPotterAndThePhilosophersStone)
library.add_book(DiaryOfAWimpyKid)
library.add_book(HitchhikersGuide)
collection = library.__str__()
print(collection)