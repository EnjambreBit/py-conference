from django.contrib import admin
from conferences.models.talk_registration import TalkRegistration


class TalkRegistrationAdmin(admin.ModelAdmin):
    model = TalkRegistration
    #list_display = (
    #    "id",
    #    "talk",
    #    "room",
     #   "date",
     #   "start",
     #   "end",
    #)
