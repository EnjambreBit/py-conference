from django.contrib import admin
from conferences.models.static_pages import StaticPage


class StaticPageAdmin(admin.ModelAdmin):
    model = StaticPage
    list_display = (
        "id",
        "title",
        "slug",
        "format",
        "published",
    )
    search_fields = ("title",)
