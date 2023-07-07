from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField
    password = serializers.CharField

class UserCreateSerializer(serializers.Serializer):
    password = serializers.CharField

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists')

