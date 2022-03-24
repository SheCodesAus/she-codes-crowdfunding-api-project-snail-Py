from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    user_id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    bio = serializers.CharField(max_length=None)
    avatar = serializers.URLField()

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)