from django.contrib import admin
from conferences.models.profiles import Profile
from conferences.models.social_media import SocialMedia


class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 0


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "is_speaker",
        "is_organizer",
    )
    search_fields = (
        "fist_name",
        "last_name",
        "user__email",
    )
    inlines = [
        SocialMediaInline,
    ]
