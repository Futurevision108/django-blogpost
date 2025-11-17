from django.shortcuts import render , get_object_or_404, redirect
from django.views import generic
from .models import Post, Comment, Category, Like

# Create your views here.
# Post list view
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"

<<<<<<< HEAD
   # Category List View
class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category_list.html"

# Likes List View
class LikesList(generic.ListView):
    queryset = Like.objects.all()
    template_name = "likes_list.html"

# Comment List View
=======

# Comment list view
>>>>>>> workingbranch
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
