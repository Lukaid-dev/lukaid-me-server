from rest_framework import serializers

from apps.posts.models import Post


class PostPinnedGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "thumbnail",
            "written_at",
        )
