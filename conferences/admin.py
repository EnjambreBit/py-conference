from django.contrib import admin

from conferences.admin_class.events import Event, EventAdmin
from conferences.admin_class.countries import Country, CountryAdmin
from conferences.admin_class.rooms import Room, RoomAdmin
from conferences.admin_class.talks import Talk, TalkAdmin
from conferences.admin_class.talk_rooms import TalkRoom, TalkRoomAdmin



# Register your models here.
admin.site.register(Country, CountryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(TalkRoom, TalkRoomAdmin)