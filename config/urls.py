from django.contrib import admin
from django.urls import include, path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


import os

ENTRY_PORT = int(os.environ.get("ENTRY_PORT", default=3030))
ORIGIN_1 = os.environ.get("ORIGIN_1")

urlpatterns = [
    path("admin/", admin.site.urls),
]

schema_view = get_schema_view(
    openapi.Info(
        title="lukaid.me API",
        default_version="v1",
        description="""
        lukaid.me API 문서입니다.
        작성자 : lukaid
        """,
        terms_of_service="",
        contact=openapi.Contact(name="lukaid", email="crescent3859@gmail.com"),
        license=openapi.License(name="lukaid.me_api_docs"),
    ),
    url=f"{ORIGIN_1}:{ENTRY_PORT}/",
    public=True,
    patterns=urlpatterns,
)

urlpatterns += [
    path(
        "swagger<str:format>",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns += [
    path("api/v1/posts/", include("apps.posts.urls")),
]
