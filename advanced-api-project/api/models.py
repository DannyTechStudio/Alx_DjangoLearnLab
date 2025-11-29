from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=150)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
    
    

"""
DOCUMENTATION:
    Author Model: The author model is responsible for defining the data structure of the author table in 
    the database with attribute like 'name' which represents the name of an author instance with maximum characters to be 100.
    
    Book Model: This model defines the data structure of the book table in the database with attributes like 'title', 'publication_year',
    and 'author' representing the title, publication year and author of a book instance. Also, the 'author' attribute of the Book model makes reference
    to the 'Author' model marking a OneToMany relationship between the 'Author' and 'Book' models which means an author can own many books 
    instances and whenever an author instance is deleted, all the books they authored willbe deleted as well. 
    
"""