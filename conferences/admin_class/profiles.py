from django.contrib import admin
from conferences.models.profiles import Profile
from conferences.models.social_media import SocialMedia
from import_export.admin import ExportMixin
from import_export import resources
from import_export.fields import Field
from import_export.formats import base_formats


class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 0


class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile


class ProfileAdmin(ExportMixin, admin.ModelAdmin):
    model = Profile
    resource_class = ProfileResource
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "country",
        "created_at",
    )
    search_fields = (
        "first_name",
        "last_name",
        "user__email",
    )
    autocomplete_fields = ("country",)
    inlines = [
        SocialMediaInline,
    ]
