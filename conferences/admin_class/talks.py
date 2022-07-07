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


class TalkAdmin(admin.ModelAdmin):
    model = Talk
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
