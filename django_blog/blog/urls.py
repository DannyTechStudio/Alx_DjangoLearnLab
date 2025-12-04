from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile

urlpatterns = [
    #--------- Login (built-in)
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    
    #--------- Logout (built-in)
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    
    #--------- Registration (custom)
    path('register/', register, name='register'),
    
    #--------- Profile page
    path('profile/', profile, name='profile'),
]
