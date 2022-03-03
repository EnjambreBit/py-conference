from django.contrib import admin
from conferences.models.events import Event


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = (
        "id",
        "name",
        "timezone",
        "start_date",
        "end_date",
    )

    def has_add_permission(self, request, obj=None):
        if Event.objects.count() > 0:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False
