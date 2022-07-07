from django.contrib import admin
from conferences.models.event_links import EventLink


class EventLinkAdmin(admin.ModelAdmin):
    model = EventLink
    list_display = (
        "id",
        "order",
        "name",
        "event",
    )
    list_filter = ("event",)
