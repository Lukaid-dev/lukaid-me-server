# custom many to many table for post and tag

from django.db import models

from apps.commons.models.common_model import CommonModel


class PostTag(CommonModel):
    """
    PostTag Model Definition
    post와 tag는 many to many 관계
    """

    class Meta:
        default_related_name = "post_tags"

    id = models.AutoField(primary_key=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"
