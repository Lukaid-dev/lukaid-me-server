from rest_framework import serializers

from apps.posts.models import Post


class PostGetSerializer(serializers.ModelSerializer):

    author = serializers.CharField(source="author.username")

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "thumbnail",
            "content",
            "author",
            "written_at",
            "is_public",
            "is_pinned",
        )
