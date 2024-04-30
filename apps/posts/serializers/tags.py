from rest_framework import serializers

from apps.posts.models import Tag


class TagsGetSerializer(serializers.ModelSerializer):

    number_of_posts = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = (
            "name",
            "number_of_posts",
        )

    def get_number_of_posts(self, obj):
        return obj.post_tags.count()
