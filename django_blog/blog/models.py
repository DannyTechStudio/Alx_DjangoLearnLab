from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering  = ['created_at']      #------ oldest first; change to '-created_at' for newest first
    
    def __str__(self):
        return f"Comment by {self.content} on {self.post}"
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    