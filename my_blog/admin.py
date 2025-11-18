from django.contrib import admin
from .models import Post, Comment, Category, Like
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
class PostAdmin (SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('status', 'created_on', 'author')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'excerpt')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'author', 'created_on', 'approved')
    search_fields = ('author__username', 'content')
    list_filter = ('approved', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected comments have been approved.")
    approve_comments.short_description = "Approve selected comments"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = ('post', 'user', 'created_on')
    search_fields = ('post__title', 'user__username')
    list_filter = ('created_on',)
