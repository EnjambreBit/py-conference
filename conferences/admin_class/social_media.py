from django.contrib import admin
from conferences.models.social_media import SocialMedia


class SocialMediaAdmin(admin.ModelAdmin):
    model = SocialMedia
    list_display = ("id", "type", "profile")
