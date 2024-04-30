from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.posts.models import Post
from apps.posts.serializers import PostsGetSerializer


class Posts(APIView):

    @swagger_auto_schema(
        operation_description="""
        # Get posts
        ## 삭제되지 않고, 공개된 모든 post를 가져옵니다.
        ## 최신순으로 정렬됩니다.
        """,
        responses={
            200: PostsGetSerializer(many=True),
        },
    )
    def get(self, request):
        queryset = Post.objects.filter(is_deleted=False, is_public=True)
        queryset = queryset.order_by("-written_at")
        serializer = PostsGetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
