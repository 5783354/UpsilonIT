from blogs.models import Blog, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class BlogSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'created_at', 'modified_at', 'title', 'description', 'image', 'amount', 'is_deleted', 'user', 'posts')