# book_class.py
class Book:
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def __del__(self):
        # Destructor that prints a message when the book instance is deleted.
        print(f"Deleting {self.title}") 
    
    def __str__(self):
        # String representation for informal display.
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        # Returning a string that would recreate the Book instance.
        return f"Book('{self.title}', '{self.author}', {self.year})"