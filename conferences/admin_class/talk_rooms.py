from django.contrib import admin
from conferences.models.talk_rooms import TalkRoom
from conferences.filters.dropdown_filter import RelatedDropdownFilter


class TalkRoomAdmin(admin.ModelAdmin):
    model = TalkRoom
    list_display = (
        "id",
        "talk",
        "room",
        "date",
        "start",
        "end",
    )
    autocomplete_fields = (
        "talk",
        "room",
    )
    list_filter = (
        ("talk", RelatedDropdownFilter),
        ("room", RelatedDropdownFilter),
    )