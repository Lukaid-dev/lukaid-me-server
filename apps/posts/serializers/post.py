from rest_framework import serializers

from apps.posts.models import Post


class PostGetSerializer(serializers.ModelSerializer):

    author = serializers.CharField(source="author.username")
    tag_list = serializers.SerializerMethodField()

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
            "tag_list",
        )

    def get_tag_list(self, obj):
        return [{"id": tag.id, "name": tag.name} for tag in obj.tags.all()]
