from django.urls import path
from apps.posts.views import PostId, PostList, PostPinned

urlpatterns = [
    path("", PostList.as_view(), name="posts"),
    path("pinned/", PostPinned.as_view(), name="posts_pinned"),
    path("<int:pk>/", PostId.as_view(), name="post"),
]
