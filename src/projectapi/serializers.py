from rest_framework import serializers
from blog.models import Category, Post, Comment, Contact
from projects.models import Project

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'