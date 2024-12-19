
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from django.conf import settings
# from django.http import Http404
from django.utils.text import slugify
from django.db.models.signals import pre_save
# from PIL import Image
# import uuid
import readtime
from django_ckeditor_5.fields import CKEditor5Field

class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    snippet = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Draft', 'Draft'), ('Published', 'Published')])
    tags = models.CharField(max_length=200, null=True, blank=True)
    slug =  models.SlugField(max_length=250, unique_for_date='publish', unique=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post')

    
    def __str__(self):
        return self.title
    
    @property
    def readtime(self):
        return readtime.of_text(self.content).text
    
    def get_readtime(self):
        # Get the readtime as minutes, ignoring the string formatting
        result = readtime.of_text(self.content)
        minutes = result.minutes
        return minutes  # Return the read time in minutes as an integer
    
    # def get_readtime(self):
    #     result = readtime.of_text(self.content)
    #     minutes = result.minutes
    #     if minutes < 60:
    #         return f"{minutes} min{'s' if minutes > 1 else ''}"
    #     else:
    #         hours = minutes // 60
    #         return f"{hours} hour{'s' if hours > 1 else ''}"
        
    # def get_readtime(self):
    #     # Example logic for calculating read time: (words count divided by 200 words per minute)
    #     words = len(self.content.split())
    #     return words // 200  # Assuming 200 words per minute reading speed
        
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug, 'pk': self.id}) # args= [self.slug, self.id]
    
    def create_slug(self, sender, instance, **kwargs):
        if not instance.slug:
            instance.slug = slugify(instance.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)