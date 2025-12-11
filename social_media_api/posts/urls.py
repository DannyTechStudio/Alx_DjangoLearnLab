from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewset, CommentViewset, UserFeedView

router = DefaultRouter()
router.register(r'posts', PostViewset)
router.register(r'comments', CommentViewset)


urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]

urlpatterns += router.urls