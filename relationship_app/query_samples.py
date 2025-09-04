import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample queries
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Quick test
if __name__ == "__main__":
    print("Books by J.K. Rowling:", list(books_by_author("J.K. Rowling")))
    print("Books in Central Library:", list(books_in_library("Central Library")))
    print("Librarian for Central Library:", librarian_for_library("Central Library"))
