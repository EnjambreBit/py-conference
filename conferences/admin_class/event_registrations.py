from django.contrib import admin
from conferences.models.event_registrations import EventRegistration


class EventRegistrationAdmin(admin.ModelAdmin):
    model = EventRegistration
    list_display = (
        "id",
        "profile",
        "event",
    )
