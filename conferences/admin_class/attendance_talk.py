from django.contrib import admin
from conferences.models.attendance_talk import AttendanceTalk
from rangefilter.filters import DateRangeFilter
from conferences.filters.dropdown_filter import RelatedDropdownFilter


from import_export.admin import ExportMixin
from import_export import resources
from import_export.fields import Field
from import_export.formats import base_formats


class AttendanceTalkResource(resources.ModelResource):
    full_name = Field(column_name="Nombre y Apellido")
    talk = Field(column_name="Workshop/Sprint")
    created_at = Field(attribute="created_at", column_name="Fecha Registro")

    class Meta:
        model = AttendanceTalk
        fields = ("full_name", "talk", "created_at")

    def dehydrate_full_name(self, obj):
        return obj.profile.full_name

    def dehydrate_talk(self, obj):
        return obj.talk_room.talk.name


class AttendanceTalkAdmin(ExportMixin, admin.ModelAdmin):
    model = AttendanceTalk
    resource_class = AttendanceTalkResource
    list_display = (
        "id",
        "profile",
        "talk_room",
        "created_at",
    )
    search_fields = (
        "profile",
        "talk_room__talk",
        "talk_room__room",
    )
    autocomplete_fields = (
        "profile",
        "talk_room",
    )
    list_filter = (
        ("talk_room__talk", RelatedDropdownFilter),
        # ("date", DateRangeFilter),
    )
