from django.db import models
from django.conf import settings

from blog.models import BlogPost

User = settings.AUTH_USER_MODEL

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(max_length=255)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.comment
