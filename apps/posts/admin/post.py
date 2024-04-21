from django.contrib import admin

from apps.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin Definition"""

    fieldsets = (
        (
            "Post",
            {
                "fields": ("title", "author", "content", "is_public", "is_pinned"),
            },
        ),
        (
            "Delete Option",
            {
                "fields": (
                    "is_deleted",
                    "deleted_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = (
        "id",
        "__str__",
    )
    list_display_links = (
        "id",
        "__str__",
    )
    search_fields = [
        "user__username",
    ]
