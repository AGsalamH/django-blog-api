from rest_framework import serializers
from django.contrib.auth import get_user_model

from blog.posts.models import Post


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)


class PostSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'creator', 'published', 'created_at', 'updated_at')
