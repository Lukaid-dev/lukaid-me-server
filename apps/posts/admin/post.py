from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.posts.admin.post_tag_admin_form import PostTagAdminForm
from apps.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin Definition"""

    def thumbnail_preview(self, obj):
        if obj.thumbnail is None:
            return "No Image"
        return mark_safe(f'<img src="{obj.thumbnail}" style="width: 50%">')

    def thumbnail_preview_list(self, obj):
        if obj.thumbnail is None:
            return "No Image"
        return mark_safe(f'<img src="{obj.thumbnail}" style="width: 100px">')

    form = PostTagAdminForm
    fieldsets = (
        (
            "Post",
            {
                "fields": (
                    "title",
                    "author",
                    "thumbnail",
                    "thumbnail_preview",
                    "content",
                    "is_public",
                    "is_pinned",
                    "category",
                ),
            },
        ),
        (
            "Date Option",
            {
                "fields": (
                    "written_at",
                    "created_at",
                    "updated_at",
                ),
            },
        ),
        (
            "Tag List",
            {
                "fields": ("TagList",),
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
    readonly_fields = (
        "author",
        "created_at",
        "updated_at",
        "deleted_at",
        "thumbnail_preview",
    )
    list_display = (
        "id",
        "__str__",
        "thumbnail_preview_list",
    )
    list_display_links = (
        "id",
        "__str__",
    )
    search_fields = [
        "user__username",
    ]
