from bookshelf.models import Book
>>> book = Book.objects.first()
>>> print("Title:", book.title)
Title: 1984
>>> print("Author:", book.author)
Author: George Orwell
>>> print("Publication Year:", book.publication_year)
Publication Year: 1949