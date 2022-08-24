from django.contrib import admin
from conferences.models.talks import Talk
from conferences.models.talk_rooms import TalkRoom
from conferences.models.speakers_per_talk import SpeakerPerTalk
from conferences.models.resources import (
    Resource,
    ResourceFile,
    ResourceImage,
    ResourceLink,
)
from import_export.admin import ExportMixin
from import_export import resources
from import_export.fields import Field
from import_export.formats import base_formats
from django.utils.html import mark_safe


class TalkRoomMediaInline(admin.TabularInline):
    model = TalkRoom
    extra = 0


class SpeakerPerTalkInline(admin.TabularInline):
    model = SpeakerPerTalk
    extra = 0


class ResourceFileInline(admin.TabularInline):
    model = ResourceFile
    extra = 0


class ResourceImageInline(admin.TabularInline):
    model = ResourceImage
    extra = 0


class ResourceLinkInline(admin.TabularInline):
    model = ResourceLink
    extra = 0


class TalkResource(resources.ModelResource):
    name = Field(attribute="name", column_name="Nombre de la charla")
    talk_type = Field(attribute="talk_type", column_name="Tipo")
    status = Field(attribute="status", column_name="Estado")
    speakers = Field(column_name="Ponentes")
    summary = Field(attribute="summary", column_name="Resumen")

    class Meta:
        model = Talk
        fields = (
            "id",
            "name",
            "talk_type",
            "status",
            "speakers",
            "summary",
        )
        export_order = (
            "id",
            "name",
            "talk_type",
            "status",
            "speakers",
            "summary",
        )

    def dehydrate_speakers(self, obj):
        speakers =[spp.speaker.profile.full_name for spp in obj.speakers_per_talk.all()]
        return ", ".join(speakers)



class TalkAdmin(ExportMixin, admin.ModelAdmin):
    model = Talk
    resource_class = TalkResource
    list_display = (
        "id",
        "event",
        "name",
        "language",
        "talk_type",
        "audience_level",
        "duration",
        "status",
    )
    search_fields = ("name",)
    inlines = [
        SpeakerPerTalkInline,
        TalkRoomMediaInline,
        ResourceFileInline,
        ResourceImageInline,
        ResourceLinkInline,
    ]
    list_filter = (
        "event",
        "talk_type",
        "status",
    )

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]

