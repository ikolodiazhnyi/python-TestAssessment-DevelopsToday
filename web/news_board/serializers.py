from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
            "comments",
        ]
        read_only_fields = ["comments"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author_name", "content", "creation_date", "post"]
