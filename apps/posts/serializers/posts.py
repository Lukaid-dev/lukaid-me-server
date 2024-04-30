from rest_framework import serializers
from utils.extract_plain_text import extract_plain_text

from apps.posts.models import Post


class PostsGetSerializer(serializers.ModelSerializer):

    content_summary = serializers.SerializerMethodField()
    tag_list = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "thumbnail",
            "content_summary",
            "written_at",
            "is_pinned",
            "tag_list",
        )

    def get_content_summary(self, obj):
        plain_text = extract_plain_text(obj.content)
        return f"{plain_text[:100]}..." if len(plain_text) > 100 else plain_text

    def get_tag_list(self, obj):
        return [
            {
                "name": post_tag.tag.name,
                "order": post_tag.order,
            }
            for post_tag in obj.post_tags.all()
        ]
