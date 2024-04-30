from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.posts.models import Tag
from apps.posts.serializers.tags import TagsGetSerializer


class Tags(APIView):

    @swagger_auto_schema(
        operation_description="""
        # Get tags
        ## 등록된 모든 tag를 가져옵니다.
        ## tag에 속한 post의 수를 함께 반환합니다.
        ## post의 수가 0이면 제외합니다.
        """,
        responses={
            200: TagsGetSerializer(many=True),
        },
    )
    def get(self, request):
        queryset = Tag.objects.all()
        serializer = TagsGetSerializer(queryset, many=True)
        serializer_data = [tag for tag in serializer.data if tag["number_of_posts"] > 0]
        return Response(serializer_data, status=status.HTTP_200_OK)
