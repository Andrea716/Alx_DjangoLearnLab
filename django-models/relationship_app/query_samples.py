from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.first()  # replace with any author you want
books_by_author = Book.objects.filter(author=author)
print("Books by author:", list(books_by_author))

# List all books in a library
library = Library.objects.first()  # replace with any library
books_in_library = library.books.all()
print("Books in library:", list(books_in_library))

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian:", librarian)
