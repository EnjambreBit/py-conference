from conferences.filters.dropdown_filter import RelatedDropdownFilter
from conferences.models.talk_rooms import TalkRoom
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from import_export.formats import base_formats
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter


class TalkRoomResource(resources.ModelResource):
    pass


class TalkRoomAdmin(admin.ModelAdmin):
    model = TalkRoom
    list_display = (
        "id",
        "talk",
        "talk_type",
        "room",
        "date_as_str",
        "start_as_str",
        "end_as_str",
    )
    autocomplete_fields = (
        "talk",
        "room",
    )
    list_filter = (
        ("talk", RelatedDropdownFilter),
        ("room", RelatedDropdownFilter),
        ("date", DateRangeFilter),
    )
