from django.shortcuts import render , get_object_or_404, redirect
from django.views import generic
from .models import Category, Like, Comment, Post
from django.contrib.auth.decorators import login_required



# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"

   # Category List View
class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category_list.html"

# Likes List View
class LikesList(generic.ListView):
    queryset = Like.objects.all()
    template_name = "likes_list.html"

# Comment List View
class CommentList(generic.ListView):
    queryset = Comment.objects.all()
    template_name = "comment_list.html"

