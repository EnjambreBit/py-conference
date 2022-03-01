from django.contrib import admin
from conferences.models.talk_rooms import TalkRoom


class TalkRoomAdmin(admin.ModelAdmin):
    model = TalkRoom
    list_display = (
        "id",
        "talk",
        "room",
        "date", 
        "start",
        "end",
    )
