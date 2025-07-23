import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Library, Author, Book

# Create data
library, _ = Library.objects.get_or_create(name='Central Library')

author, _ = Author.objects.get_or_create(name='George Orwell')

book1, _ = Book.objects.get_or_create(title='1984', author=author, library=library)
book2, _ = Book.objects.get_or_create(title='Animal Farm', author=author, library=library)

# Query books by library name
library_name = 'Central Library'
library = Library.objects.get(name=library_name)  # ✅ required line

books = library.books.all()  # ✅ required line

print(f"Books by {author.name} in {library.name}:")
for book in books:
    if book.author == author:
        print(f"- {book.title}")
