from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter 
from rest_framework.filters import OrderingFilter
from .models import Book
from .serializers import BookSerializer


#------------ ListView for retrieving all books
"""
Handles the creation of new Book records where only authenticated users can create
"""
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]     #-------- Anyone can view
    
    # Filtering, Searching & Ordering Features enabled
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    
    # Filtering
    filterset_fields = ['title', 'publication_year', 'author']
    
    # Searching
    search_fields = ['title', 'author_name']
    
    # Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


#------------ DetailView for retrieving a single book by ID
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]     #-------- Anyone can view


#------------ CreateView for adding a new book
"""
Handles the creation of new Book records where 
only authenticated users can create
"""
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]        #-------- Only authenticted users
    
    #--------- Customize behavior on create
    def perform_create(self, serializer):
        # Example: attach logged-in user as 'creator'
        serializer.save(create_by=self.request.user)


#------------ UpdateView for modifying an existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]      #-------- Only authenticated users

    #--------- Customize behavior on update
    def perform_create(self, serializer):
        # Example: record last modifier
        serializer.save(last_modified_by=self.request.user)


#------------ DeleteView for removing a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]      #-------- Only authenticated users