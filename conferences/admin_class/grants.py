from re import search
from django.contrib import admin
from conferences.models.grants import Grant


class GrantAdmin(admin.ModelAdmin):
    model = Grant
    list_display = (
        "id",
        "profile",
        "event",
        "status",
        "request_amount_str",
        "approbed_amount_str",
        "paid"
    )
    search_fields = (
        "profile__first_name",
        "profile__last_name",
    )
    autocomplete_fields = (
        "profile", 
        "event",
        "approbed_by",
        "paid_by",
    )