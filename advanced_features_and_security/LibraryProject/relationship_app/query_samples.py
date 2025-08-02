import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Library, Author, Book

# Create or get data
library, _ = Library.objects.get_or_create(name='Central Library')
author, _ = Author.objects.get_or_create(name='George Orwell')

Book.objects.get_or_create(title='1984', author=author, library=library)
Book.objects.get_or_create(title='Animal Farm', author=author, library=library)

# Query author by name (required exact line)
author_name = 'George Orwell'
author = Author.objects.get(name=author_name)  # required line

# Query books by that author (required exact line)
books = Book.objects.filter(author=author)  # required line

print(f"Books by {author.name}:")
for book in books:
    print(f"- {book.title}")

# Query library by name
library_name = 'Central Library'
library = Library.objects.get(name=library_name)

# Get all books in library
books_in_library = library.books.all()

print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print(f"- {book.title}")

# Retrieve librarian for library if exists (optional)
from relationship_app.models import Librarian

try:
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian of {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"\nNo librarian found for {library.name}")
