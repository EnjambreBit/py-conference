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
    talk = Field(attribute="talk", column_name="Charla")
    room = Field(attribute="room", column_name="Aula")
    start = Field(attribute="start", column_name="Inicio")
    end = Field(attribute="end", column_name="Inicio")
    date = Field(attribute="date", column_name="Fecha")
    registered = Field(column_name="Registrados")
    attendance = Field(column_name="Asistencia")

    class Meta:
        model = TalkRoom
        fields = (
            "talk",
            "room",
            "date",
            "start",
            "end",
            "registered",
            "attendance",
        )

    def dehydrate_registered(self, obj):
        return obj.talk.talks_registrations.all().count()

    def dehydrate_attendance(self, obj):
        return obj.attendance_talks.all().count()


class TalkRoomAdmin(ExportMixin, admin.ModelAdmin):
    model = TalkRoom
    resource_class = TalkRoomResource

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
        "talk__name",
        "room__name",
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

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "talk":
    #         kwargs["queryset"] = Talk.objects.filter(status="published")
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
