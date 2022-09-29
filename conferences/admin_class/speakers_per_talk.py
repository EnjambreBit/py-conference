from django.contrib import admin
from conferences.models.speakers_per_talk import SpeakerPerTalk
from conferences.filters.dropdown_filter import RelatedDropdownFilter


class SpeakerPerTalkAdmin(admin.ModelAdmin):
    model = SpeakerPerTalk
    list_display = (
        "id",
        "speaker",
        "talk",
    )
    autocomplete_fields = (
        "talk",
        "speaker",
    )
    list_filter = (("talk", RelatedDropdownFilter),)
