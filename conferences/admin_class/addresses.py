from django.contrib import admin
from conferences.models.addresses import Address


class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = (
        "id",
        "name",
        "address_line_1",
        "address_line_2",
        "city",
        "state",
        "country",
        "zipcode",
    )
    autocomplete_fields = ("country",)
