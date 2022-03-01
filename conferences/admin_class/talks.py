from django.contrib import admin
from conferences.models.talks import Talk
from conferences.models.resources import Resource
from conferences.models.talk_rooms import TalkRoom
from conferences.models.speakers_per_talk import SpeakerPerTalk


class TalkRoomMediaInline(admin.TabularInline):
    model = TalkRoom
    extra = 0

class SpeakerPerTalkInline(admin.TabularInline):
    model = SpeakerPerTalk
    extra = 0

class ResourceMediaInline(admin.TabularInline):
    model = Resource
    extra = 0

class TalkAdmin(admin.ModelAdmin):
    model = Talk
    list_display = (
        "id",
        "name",
        "language",
        "talk_type",
        "audience_level",
        "duration",
        "published",
    )
    search_fields = (
        "name",
    )
    inlines = [
        SpeakerPerTalkInline,
        TalkRoomMediaInline,
        ResourceMediaInline,
    ]