from django.contrib import admin
from conferences.models.talks import Talk


class TalkAdmin(admin.ModelAdmin):
    model = Talk
    list_display = (
        'id',
        'name',
        'language',
        'talk_type',
        'audience_level',
        'duration',
    )

