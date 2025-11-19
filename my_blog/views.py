from django.shortcuts import render , get_object_or_404, redirect
from django.views import generic
from .models import Post, Comment, Category, Like


# Post list view


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 3


# Category List View
class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category_list.html"
    queryset = Category.objects.all()


# Likes List View
class LikesList(generic.ListView):
    queryset = Like.objects.all()
    template_name = "likes_list.html"


# Comment List View
class CommentList(generic.ListView):
    queryset = Comment.objects.all()
    template_name = "comment_list.html"

