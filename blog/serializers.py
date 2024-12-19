from django.conf import settings
from rest_framework import serializers
from .models import Posts
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # This gets the User model based on the AUTH_USER_MODEL setting
        fields = ['id', 'first_name', 'last_name', 'profile_picture', 'is_staff', 'is_active',]


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # This gets the User model based on the AUTH_USER_MODEL setting
        fields = ['id']


class PostsSerializer(serializers.ModelSerializer):
    read_time = serializers.SerializerMethodField()
    author_info = serializers.SerializerMethodField()
    class Meta:
        model = Posts
        fields = ['id', 'title', 'snippet', 'content' ,'image','status','tags', 'created_at', 'publish','read_time','slug','author', 'author_info']

    def get_read_time(self, obj):
        return obj.get_readtime()
    
    def get_author_info(self, obj):
        author = obj.author
        # Construct the full URL for the profile picture
        profile_picture_url = author.profile_picture.url if author.profile_picture else None

        if profile_picture_url:
            profile_picture_url = settings.BASE_URL + profile_picture_url

        return {
            'id': author.id,
            'full_name': f'{author.first_name} {author.last_name}',
            'profile_picture': profile_picture_url,
        }



class PostCreateSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
    class Meta:
        model = Posts
        fields = ['id', 'title', 'snippet', 'content','image','status','tags', 'author']
