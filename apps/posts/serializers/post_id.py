from rest_framework import serializers

from apps.posts.models import Post


class PostIdGetSerializer(serializers.ModelSerializer):

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
        return [
            {
                "name": post_tag.tag.name,
                "order": post_tag.order,
            }
            for post_tag in obj.post_tags.all()
        ]
