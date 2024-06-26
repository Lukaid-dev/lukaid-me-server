from django.urls import path
from apps.posts.views import PostId, Posts, PostsAll, PostsPinned, PostsByTag, Tags

urlpatterns = [
    path("", Posts.as_view(), name="posts"),
    path("all/", PostsAll.as_view(), name="posts_all"),
    path("pinned/", PostsPinned.as_view(), name="posts_pinned"),
    path("<int:pk>/", PostId.as_view(), name="post_id"),
    path("tag/<str:tag_name>/", PostsByTag.as_view(), name="posts_by_tag"),
    path("tags/", Tags.as_view(), name="tags"),
]
