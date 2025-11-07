from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.
# Function-based views
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# class based-views
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view (built-in)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view (built-in)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'