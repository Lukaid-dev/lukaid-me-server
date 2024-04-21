from django.urls import path
from apps.posts.views import (
    Posts,
    PostId,
)

urlpatterns = [
    path("<int:pk>/", PostId.as_view(), name="post"),
    path("", Posts.as_view(), name="posts"),
]
