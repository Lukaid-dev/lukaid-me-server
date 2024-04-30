from django.contrib import admin

from apps.posts.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag Admin Definition"""

    fieldsets = (
        (
            "Tag",
            {
                "fields": ("name",),
            },
        ),
    )
    list_display = ("name",)
    search_fields = ("name",)
