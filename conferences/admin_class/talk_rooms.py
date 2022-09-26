from conferences.filters.dropdown_filter import RelatedDropdownFilter
from conferences.models.talk_rooms import TalkRoom
from conferences.models.talks import Talk
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
    search_fields = (
        "talk",
        "room",
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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "talk":
            kwargs["queryset"] = Talk.objects.filter(status="published")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)