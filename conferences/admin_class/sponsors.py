from django.contrib import admin
from conferences.models.sponsors import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor
    list_display = (
        "id",
        "event",
        "name",
        "sponsor_level",
        "confirmed",
        "published",
    )
    search_fields = ("name",)
    list_filter =("event", "sponsor_level",)