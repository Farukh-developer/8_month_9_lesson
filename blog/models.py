from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    theme=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.theme

class Likes(models.Model):
    likes=models.BooleanField()
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.blog.theme} - {self.likes}"



class Comments(models.Model):
    text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Comment by {self.user.username}"

    