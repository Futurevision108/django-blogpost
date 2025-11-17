from django.shortcuts import render
from django.views import generic
from .models import Post, Comment, Category, Like


# Create your views here.
# Post list view
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"


# Comment list view
class CommentList(generic.ListView):
    queryset = Comment.objects.all()
    template_name = "comment_list.html"


# Category list view
class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category_list.html"


# Likes list view
class LikesList(generic.ListView):
    queryset = Like.objects.all()
    template_name = "likes_list.html"
