from django.contrib import admin
from conferences.models.rooms import Room


class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = (
        "id",
        "name",
        "internal_name",
        "capacity",
    )
