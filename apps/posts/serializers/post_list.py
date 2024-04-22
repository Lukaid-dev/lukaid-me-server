from rest_framework import serializers

from apps.posts.models import Post
from utils.extract_plain_text import extract_plain_text


class PostListGetSerializer(serializers.ModelSerializer):
    content_summary = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "thumbnail",
            "content_summary",
            "written_at",
            "is_pinned",
        )

    def get_content_summary(self, obj):
        plain_text = extract_plain_text(obj.content)
        return f"{plain_text[:100]}..." if len(plain_text) > 100 else plain_text
