from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

# from apps.commons.views.pagination import Pagination TODO: 추후 구현

from apps.posts.serializers import (
    PostGetSerializer,
)
from apps.posts.models import Post


class Posts(APIView):

    @swagger_auto_schema(
        operation_description="""
        # Get posts
        ## 우선은 모든 post
        """,
    )
    def get(self, request):
        queryset = Post.objects.filter(is_deleted=False)
        queryset = queryset.order_by("-updated_at")
        serializer = PostGetSerializer(queryset, many=True)
        return Response(serializer.data)
