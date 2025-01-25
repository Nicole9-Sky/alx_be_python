class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
    
class EBook(Book):
    def __init__(self, title, author, full_sizes):
        super().__init__(title, author)
        self.full_sizes = full_sizes
        
        def __str__(self):
            return f"EBook: {self.title} by {self.author}, full_sizes: {full_sizes}"
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
        
        def __str__(self):
            return f"PrintBook: {self.title} by {self.author}, page_count: {page_count}"
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        # Add a book to the library.
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("only instances of Book or its subclasses can be added to the library.")
    def list_books(self):
        for book in self.books:
            print(book)
        