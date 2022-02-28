from django.contrib import admin
from conferences.models.events import Event


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = (
        'id',
        'name',
        'timezone',
        'start_date',
        'end_date',
    )

