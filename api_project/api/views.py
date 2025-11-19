from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book 

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
      
        
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)       # Automatically set the author to the logged-in user