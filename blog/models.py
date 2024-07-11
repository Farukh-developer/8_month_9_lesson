from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    theme=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
class Likes(models.Model):
    likes=models.BooleanField()
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(Blog, on_delete=models.CASCADE)
    