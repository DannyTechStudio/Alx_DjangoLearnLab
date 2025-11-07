from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
# Function-based views
def get_book_lists(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'list_books.html', context)

# class based-views
class get_library_details(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
