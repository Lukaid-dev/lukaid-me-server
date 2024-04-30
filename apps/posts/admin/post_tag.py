from django.contrib import admin

from apps.posts.models import PostTag


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    """PostTag Admin Definition"""

    fieldsets = (
        (
            "PostTag",
            {
                "fields": ("post", "tag", "order"),
            },
        ),
    )
    list_display = ("post", "tag", "order")
    search_fields = ("post", "tag")
    list_filter = ("post", "tag")
    list_display_links = ("post", "tag")
    list_editable = ("order",)
