from rest_framework import viewsets, permissions
from projects.models import Project
from blog.models import Category, Post, Comment, Contact
from .serializers import CategorySerializers, PostSerializers, CommentSerializers, ContactSerializers, ProjectSerializers

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializers

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializers

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentSerializers

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProjectSerializers
