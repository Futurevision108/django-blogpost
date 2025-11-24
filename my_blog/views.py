from django.shortcuts import render, get_object_or_404, redirect

from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Category, Like


# Post list view


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3

# Post detail view
def post_detail(request, slug):
    """
    Display a single blog post:model:`my_blog.Post` along with its comments.

    **Context**
    ``post``
        An instance of :model:`my_blog.Post`.

    **Template:**
    :template:`blog/post_detail.html`

    """
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = Comment.objects.filter(post=post)
    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
    },
    )


# Category List View
class CommentList(generic.ListView):
    queryset = Comment.objects.all()
    template_name = "comment_list.html"


class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category_list.html"


class LikesList(generic.ListView):
    queryset = Like.objects.all()
    template_name = "likes_list.html"


@login_required
def like_post(request, slug):
    """Toggle like/unlike for the current user on a post and redirect back.

    The URL pattern uses a `slug` parameter so we accept `slug` here.
    """
    if request.method == 'POST':
        post = get_object_or_404(Post, slug=slug, status=1)
        existing = Like.objects.filter(post=post, user=request.user).first()
        if existing:
            existing.delete()
        else:
            Like.objects.create(post=post, user=request.user)
    return redirect('post_detail', slug=slug)
