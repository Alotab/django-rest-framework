from django.contrib import admin
from .models import Comment, Posts as CreatePost

@admin.register(CreatePost)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # list_display = ['user_comment', 'comment', 'blog']
    list_display = ['comment', 'blog']