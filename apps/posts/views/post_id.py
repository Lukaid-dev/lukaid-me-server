from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.posts.models import Post
from apps.posts.serializers import PostIdGetSerializer


class PostId(APIView):

    @swagger_auto_schema(
        operation_description="""
        # Get post
        ## id를 기준으로 하나의 post를 가져옵니다.
        """,
        responses={
            200: PostIdGetSerializer(),
        },
    )
    def get_object(self, pk):
        try:
            post = Post.objects.get(id=pk)
            if post.is_deleted:
                raise exceptions.NotFound
            if not post.is_public:
                raise exceptions.NotFound
            return post
        except post.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, pk, format=None):
        post = self.get_object(pk)

        if post.is_public is False:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostIdGetSerializer(post)

        return Response(serializer.data, status=status.HTTP_200_OK)
