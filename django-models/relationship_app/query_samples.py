import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # adjust if your settings file is elsewhere
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

from relationship_app.models import Author, Book, Library

library, _ = Library.objects.get_or_create(name="Central Library")
author, _ = Author.objects.get_or_create(name="George Orwell")

Book.objects.get_or_create(title="1984", author=author, library=library)
Book.objects.get_or_create(title="Animal Farm", author=author, library=library)

print("Books by George Orwell:")
for book in author.book_set.all():
    print(book.title)

