from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.posts.serializers import (
    PostPinnedGetSerializer,
)
from apps.posts.models import Post


class PostPinned(APIView):

    @swagger_auto_schema(
        operation_description="""
        Get all pinned posts.
        """,
    )
    def get(self, request):
        queryset = Post.objects.filter(is_deleted=False, is_pinned=True, is_public=True)
        queryset = queryset.order_by("-written_at")
        serializer = PostPinnedGetSerializer(queryset, many=True)
        return Response(serializer.data)
