from django.db import models

from apps.commons.models.common_model import CommonModel


class Category(CommonModel):
    """
    Category Model Definition
    post와 category는 many to one 관계
    """

    class Meta:
        default_related_name = "categories"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
