from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.posts.models import Post
from apps.posts.serializers import PostsPinnedGetSerializer


class PostsPinned(APIView):

    @swagger_auto_schema(
        operation_description="""
        # Get pinned posts
        ## 고정된 post를 가져옵니다.
        ## 최신순으로 정렬됩니다.
        """,
        responses={
            200: PostsPinnedGetSerializer(many=True),
        },
    )
    def get(self, request):
        queryset = Post.objects.filter(is_deleted=False, is_pinned=True, is_public=True)
        queryset = queryset.order_by("-written_at")
        serializer = PostsPinnedGetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
