from rest_framework import serializers
from django.contrib.auth import get_user_model

from blog.posts.models import Post


UserModel = get_user_model()

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username',)


class PostSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'creator', 'published', 'created_at', 'updated_at')
