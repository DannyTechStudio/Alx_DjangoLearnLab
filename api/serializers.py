from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

"""
DOCUMENTATION:
    The **one-to-many relationship** between the `Author` and `Book` models is managed by **nesting the `BookSerializer` inside the 
    `AuthorSerializer`**. This means that every time an `Author` instance is serialized, Django REST Framework automatically includes 
    a fully serialized list of all the `Book` objects associated with that author. In other words, the related books are represented directly 
    inside the parent author's serialized output, providing a complete and hierarchical view of the relationship.
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
    def validate(self, data):
        current_year = datetime.now().year
        
        if data['publication_year'] > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
        return data



class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        field = ['id', 'name', 'books']