from .models import ShortenedURL
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['url', 'username', 'email', 'is_staff']