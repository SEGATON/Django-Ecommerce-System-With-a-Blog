from django.urls import path
from . import views  


app_name = 'blog'

urlpatterns = [
    path('blog_posts/', views.blog_posts, name='blog_posts'),
    path('<slug:single_post>/',views.single_post, name='single_post'),




]
