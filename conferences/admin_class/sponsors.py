from django.contrib import admin
from conferences.models.sponsors import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor
    list_display = (
        'id',
        'name',
        'sponsor_level',
    )

