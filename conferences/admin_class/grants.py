from re import search
from django.contrib import admin
from conferences.models.grants import Grant


class GrantAdmin(admin.ModelAdmin):
    model = Grant
    list_display = (
        'id',
        'profile',
        'status',
    )
    search_fields = ("profile__first_name", "profile__last_name",)
