from django.contrib import admin

# Register your models here.
from .models import Blog, Likes, Comments

admin.site.register([Blog, Likes, Comments])