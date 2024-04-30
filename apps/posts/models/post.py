from django.db import models
from django.utils import timezone

from apps.commons.models.common_model import CommonModel


class Post(CommonModel):
    """
    Post Model Definition
    Markdown을 저장하는 Post 모델
    """

    class Meta:
        default_related_name = "posts"

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    thumbnail = models.CharField(null=True, blank=True)
    content = models.TextField()
    written_at = models.DateTimeField(default=timezone.now, null=True, blank=True)

    is_public = models.BooleanField(default=True)
    is_pinned = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    author = models.ForeignKey("users.User", on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    tags = models.ManyToManyField("Tag", blank=True, through="PostTag")

    def __str__(self):
        return self.title
