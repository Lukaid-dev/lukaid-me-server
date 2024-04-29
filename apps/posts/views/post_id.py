from django.utils import timezone

from rest_framework import status
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# from drf_yasg import openapi

from apps.posts.serializers import PostGetSerializer
from apps.posts.models import Post


class PostId(APIView):

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

    @swagger_auto_schema(
        operation_description="""
        # post를 가져옵니다.
        ### - 요청한 포스트가 삭제되었다면 404를 반환합니다.
        ### - 요청한 포스트가 비공개라면 404를 반환합니다.
        """,
        responses={
            200: PostGetSerializer(),
        },
    )
    def get(self, request, pk, format=None):
        post = self.get_object(pk)

        if post.is_public is False:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostGetSerializer(
            post,
            context={"request": request},
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
