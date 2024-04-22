from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.posts.models import Post
from apps.posts.serializers.post_list import PostListGetSerializer


class PostList(APIView):

    @swagger_auto_schema(
        operation_description="""
        # Get posts
        ## 우선은 모든 post
        """,
    )
    def get(self, request):
        queryset = Post.objects.filter(is_deleted=False)
        queryset = queryset.order_by("-written_at")
        serializer = PostListGetSerializer(queryset, many=True)
        return Response(serializer.data)
