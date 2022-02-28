from django.contrib import admin
from conferences.models.countries import Country


class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = (
        'id',
        'name',
        'alpha_2',
        'alpha_3',
    )

