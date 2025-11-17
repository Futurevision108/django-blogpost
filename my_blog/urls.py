from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('category/', views.CategoryList.as_view(), name='category_list'),
    path('likes/', views.LikesList.as_view(), name='likes_list'),
]
