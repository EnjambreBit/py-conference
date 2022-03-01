from django.contrib import admin
from conferences.models.sponsor_levels import SponsorLevel


class SponsorLevelAdmin(admin.ModelAdmin):
    model = SponsorLevel
    list_display = (
        'id',
        'name',
    )

