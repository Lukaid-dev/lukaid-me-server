from rest_framework import serializers

from apps.posts.models import Post


class PostGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "created_at",
            "updated_at",
            "is_public",
            "is_pinned",
        )
