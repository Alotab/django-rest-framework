from django.contrib.auth.models import User
from rest_framework import serializers

from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model


# class CustomUserSerializer(UserSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'first_name', 'last_name']
#         # fields = ['id', 'email', 'username', 'first_name', 'last_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

        def create(self, validated_date):
            user = User.objects.create_user(**validated_date)
            return user