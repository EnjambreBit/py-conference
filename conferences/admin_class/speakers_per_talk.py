from django.contrib import admin
from conferences.models.speakers_per_talk import SpeakerPerTalk


class SpeakerPerTalkAdmin(admin.ModelAdmin):
    model = SpeakerPerTalk
    list_display = (
        "id",
        "talk",
        "speaker",
    )
    autocomplete_fields = ("talk", "speaker")
