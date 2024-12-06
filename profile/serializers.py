from django.contrib.auth.models import User
from rest_framework import serializers








class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def create(self, validated_date):
            user = User.objects.create_user(**validated_date)
            return user