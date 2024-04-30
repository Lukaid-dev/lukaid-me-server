# many to many relationship between posts and tags

from django.db import models

from apps.commons.models.common_model import CommonModel


class Tag(CommonModel):
    """
    Tag Model Definition
    post와 tag는 many to many 관계
    """

    class Meta:
        default_related_name = "tags"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
