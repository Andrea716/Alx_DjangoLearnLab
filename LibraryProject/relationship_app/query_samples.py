from relationship_app.models import Author, Book, Library, Librarian

# Sample data creation (run once in Django shell)
# author = Author.objects.create(name="George Orwell")
# book1 = Book.objects.create(title="1984", author=author)
# book2 = Book.objects.create(title="Animal Farm", author=author)
# library = Library.objects.create(name="Central Library")
# library.books.set([book1, book2])
# librarian = Librarian.objects.create(name="Alice", library=library)

# 1. Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by", author_name, ":", list(books_by_author))

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in library", library_name, ":", list(books_in_library))

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian for", library_name, ":", librarian)
