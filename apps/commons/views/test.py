from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views import Pagination
from apps.posts.models.post import Post
from apps.posts.serializers.posts import PostsGetSerializer

pagination = Pagination(0, 10)


class Test(APIView):
    """
    # api test용
    - 단순 테스트용입니다. 신경쓰지 마세요.
    """

    @swagger_auto_schema(
        operation_description="""
        # For Test
        ## Test 1 - post를 pagination하여 가져 온다.
        반환 목록
        {
            "start": 0,
            "offset": 10,
            "next": 10,
            "posts": [...],
        }
        ### - 다음 요청시에는 next값을 start로 요청해주세요!
        ### - next가 null이면 더이상 요청할 데이터가 없습니다.
        """,
        manual_parameters=pagination.get_params,
    )
    def get(self, request):

        queryset = Post.objects.filter(is_deleted=False, is_public=True).order_by(
            "-written_at"
        )
        result = pagination.get(request, queryset)
        serializer = PostsGetSerializer(
            result.pop("result"),
            many=True,
            context={"request": request},
        )

        result["posts"] = serializer.data

        return Response(result, status=status.HTTP_200_OK)
