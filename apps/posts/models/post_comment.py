# 당장은 로그인 없이 구현할거라 사용하지 않을 모델이지만 추후에 사용할 수 있도록 구현해둠

from django.db import models
from apps.commons.models.common_model import CommonModel


class PostComment(CommonModel):
    """PostComment Model Definition"""

    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        if self.parent:
            return f"Re: {self.parent} - {self.user.username}"  # 대댓글 표시
        else:
            return f"{self.user.username} comments {self.post}"
