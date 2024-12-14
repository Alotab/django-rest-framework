from rest_framework import serializers
from .models import Posts
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # This gets the User model based on the AUTH_USER_MODEL setting
        fields = ['id', 'first_name', 'last_name', 'profile_picture']


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # This gets the User model based on the AUTH_USER_MODEL setting
        fields = ['id']


class PostsSerializer(serializers.ModelSerializer):
    read_time = serializers.SerializerMethodField()
    author_info = serializers.SerializerMethodField()
    class Meta:
        model = Posts
        fields = ['id', 'title', 'snippet', 'content' ,'image','status','tags','publish','read_time','slug','author', 'author_info']

    def get_read_time(self, obj):
        return obj.get_readtime()
    
    def get_author_info(self, obj):
        author = obj.author

        return {
            'id': author.id,
            'full_name': f'{author.first_name} {author.last_name}',
            'profile_picture': author.profile_picture.url if author.profile_picture else None,
        }



class PostCreateSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
    class Meta:
        model = Posts
        fields = ['id', 'title', 'snippet', 'content' ,'image','status','tags', 'author']
