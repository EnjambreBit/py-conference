from re import search
from django.contrib import admin
from conferences.models.speakers import Speaker


class SpeakerAdmin(admin.ModelAdmin):
    model = Speaker
    list_display = (
        'id',
        'profile',
    )
    search_fields = (
        'profile__first_name', 
        'profile__last_name',
    )
