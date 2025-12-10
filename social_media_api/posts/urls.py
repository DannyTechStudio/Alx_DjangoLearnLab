from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewset, CommentViewset

router = DefaultRouter()
router.register(r'posts', PostViewset)
router.register(r'comments', CommentViewset)

urlpatterns = router.urls
