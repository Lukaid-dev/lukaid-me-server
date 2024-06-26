from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views.pagination import Pagination
from apps.posts.models import Post
from apps.posts.serializers import PostsGetSerializer

pagination = Pagination(0, 10)


class Posts(APIView):

    @swagger_auto_schema(
        operation_description="""
        # Get posts by 10
        ## 삭제되지 않고, 공개된 post를 최신순으로 10개 단위로 가져옵니다.
        ### - 다음 요청시에는 next값을 start로 요청해주세요!
        ### - next가 null이면 더이상 요청할 데이터가 없습니다.
        """,
        manual_parameters=pagination.get_params,
        responses={
            200: PostsGetSerializer(many=True),
        },
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
