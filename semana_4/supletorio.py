class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return [book.title for book in self.books]

    def __str__(self):
        return f"Author: {self.name}, Books: {', '.join(self.get_books()) if self.books else 'No books yet'}"


class Book:
    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author
        author.add_book(self)  # Asocia el libro con el autor automáticamente

    def __str__(self):
        return f"'{self.title}' by {self.author.name}, {self.pages} pages"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books_by_author(self, author_name):
        return [book for book in self.books if book.author.name == author_name]

    def __str__(self):
        if not self.books:
            return "The library has no books."
        return f"Library contains {len(self.books)} books: " + ", ".join([book.title for book in self.books])


# Ejemplo de uso

# Crear autores
author1 = Author("Gabriel García Márquez")
author2 = Author("Isabel Allende")

# Crear libros y asociarlos a los autores
book1 = Book("Cien años de soledad", 471, author1)
book2 = Book("El amor en los tiempos del cólera", 368, author1)
book3 = Book("La casa de los espíritus", 481, author2)

# Crear una biblioteca
library = Library()

# Agregar libros a la biblioteca
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Listar los libros de un autor en particular
print(f"Libros de {author1.name}: {author1.get_books()}")  # Libros de Gabriel García Márquez
print(f"Libros de {author2.name}: {author2.get_books()}")  # Libros de Isabel Allende

# Ver los libros en la biblioteca
print(library)

# Listar libros de un autor por su nombre
books_by_author = library.get_books_by_author("Gabriel García Márquez")
print(f"Libros en la biblioteca de Gabriel García Márquez: {[str(book) for book in books_by_author]}")
