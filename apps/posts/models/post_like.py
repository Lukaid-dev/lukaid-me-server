# 당장은 로그인 없이 구현할거라 사용하지 않을 모델이지만 추후에 사용할 수 있도록 구현해둠

from django.db import models
from apps.commons.models.common_model import CommonModel


class PostLike(CommonModel):
    """PostLike Model Definition"""

    class Meta:
        default_related_name = "post_likes"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} likes {self.post}"
