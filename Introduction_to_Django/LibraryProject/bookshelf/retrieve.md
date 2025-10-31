# Retrieving book instance

from bookshelf.models import Book

Book.objects.all()

# <QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>