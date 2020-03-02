from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contactfemi, name='contactfemi'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<category>/', views.blog_category, name='blog_category'),
    
]