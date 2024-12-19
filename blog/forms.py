from django import forms
from taggit.managers import TaggableManager
from .models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title','snippet','content','image', 'status','tags', )
        prepopulated_fields = {'slug': ('title',)}
