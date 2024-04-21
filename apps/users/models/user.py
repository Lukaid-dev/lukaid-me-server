# in config/settings.py : AUTH_USER_MODEL = 'users.User'
# 로그인 기능을 넣을 것 같지는 않지만, 혹시 모르니까 User 모델을 만들어놓자. (나중에 추가할 때 귀찮다.)

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        default_related_name = "users"

    id = models.AutoField(primary_key=True)
    firebase_picture = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        default="",
    )

    username = models.CharField(max_length=30, unique=True)

    first_name = None
    last_name = None

    # delete option
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}_{self.username}"
