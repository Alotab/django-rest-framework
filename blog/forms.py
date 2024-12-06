from django import forms
from taggit.managers import TaggableManager
from .models import Posts
# from .models import Comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')



class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title','snippet','content','image', 'status','tags', )
        prepopulated_fields = {'slug': ('title',)}
