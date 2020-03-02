from django.contrib import admin
from .models import Category, Post, Comment, Contact

blogModel = [Category, Post, Comment, Contact]

admin.site.register(blogModel)