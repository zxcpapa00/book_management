from django.contrib.auth import get_user_model
from rest_framework import serializers

user_model = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""
    class Meta:
        model = user_model
        fields = ['first_name', 'username', 'email', 'password']
