class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book:'Book'):
        self.books.append(book)

#________________________________

class Book:
    def __init__(self, title:str, pages:str,author):
        self.title = title
        self.pages = pages
        self.author =author
    def __str__(self):
        return f"Libro:(self.title)"

#________________________________

class Library:
    def __init__(self):
        self.book = []


author_1 = Author(name='Gabriel Garcia Marquez')

book_1 = Book('Cien años de soledad', 473, author_1)

#________________________________
