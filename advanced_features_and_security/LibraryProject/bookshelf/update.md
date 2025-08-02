>>> from bookshelf.models import Book
>>> book = Book.objects.first()
>>> print("Title:", book.title)
Title: 1984
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print("Title:", book.title)
Title: Nineteen Eighty-Four