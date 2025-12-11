from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewset, CommentViewset, user_feed

router = DefaultRouter()
router.register(r'posts', PostViewset)
router.register(r'comments', CommentViewset)


urlpatterns = [
    path('feed/', user_feed, name='user-feed'),
]

urlpatterns += router.urls