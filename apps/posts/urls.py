from django.urls import path
from apps.posts.views import PostId, Posts, PostsPinned

urlpatterns = [
    path("", Posts.as_view(), name="posts"),
    path("pinned/", PostsPinned.as_view(), name="posts_pinned"),
    path("<int:pk>/", PostId.as_view(), name="post_id"),
]
