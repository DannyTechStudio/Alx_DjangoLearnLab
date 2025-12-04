from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),           #--------- Login (built-in)
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),       #--------- Logout (built-in
    path('register/', register, name='register'),       #--------- Registration (custom)
    path('profile/', profile, name='profile'),          #--------- Profile page
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
