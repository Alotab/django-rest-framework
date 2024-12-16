from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'profile_picture', 'is_staff', 'is_active',]

        def create(self, validated_date):
            user = User.objects.create_user(**validated_date)
            return user