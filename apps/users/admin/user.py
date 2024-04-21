from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    form = UserAdmin.form
    fieldsets = (
        (
            "Profile",
            {
                "fields": ("username",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
            },
        ),
    )
    readonly_fields = (
        "username",
        "last_login",
        "date_joined",
    )
    list_display = (
        "id",
        "username",
    )
    list_display_links = (
        "id",
        "username",
    )
    search_fields = ("username",)
