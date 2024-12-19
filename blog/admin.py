from django.contrib import admin
from .models import Posts as CreatePost

@admin.register(CreatePost)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title', )}