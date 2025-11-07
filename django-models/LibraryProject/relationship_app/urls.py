from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_book_lists, name='book_list'),
    path('library/<int:pk>/', views.get_library_details.as_view(), name='library_detail'),
]
