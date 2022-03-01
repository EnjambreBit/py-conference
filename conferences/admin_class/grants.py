from django.contrib import admin
from conferences.models.grants import Grant


class GrantAdmin(admin.ModelAdmin):
    model = Grant
    list_display = (
        'id',
        'profile',
        'status',
    )

