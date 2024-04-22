from django.urls import path
from apps.posts.views import (
    PostId,
    PostList,
)

urlpatterns = [
    path("<int:pk>/", PostId.as_view(), name="post"),
    path("", PostList.as_view(), name="posts"),
]
