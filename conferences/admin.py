from django.contrib import admin

from conferences.admin_class.events import Event, EventAdmin
from conferences.admin_class.countries import Country, CountryAdmin
from conferences.admin_class.rooms import Room, RoomAdmin
from conferences.admin_class.talks import Talk, TalkAdmin
from conferences.admin_class.talk_rooms import TalkRoom, TalkRoomAdmin
from conferences.admin_class.profiles import Profile, ProfileAdmin
from conferences.admin_class.speakers import Speaker, SpeakerAdmin
from conferences.admin_class.social_media import SocialMedia, SocialMediaAdmin
from conferences.admin_class.speakers_per_talk import (
    SpeakerPerTalk,
    SpeakerPerTalkAdmin,
)
from conferences.admin_class.contact_information import (
    ContactInformation,
    ContactInformationAdmin,
)
from conferences.admin_class.sponsor_levels import SponsorLevel, SponsorLevelAdmin
from conferences.admin_class.sponsors import Sponsor, SponsorAdmin
from conferences.admin_class.grants import Grant, GrantAdmin
from conferences.admin_class.static_pages import StaticPage, StaticPageAdmin
from conferences.admin_class.resources import (
    Resource,
    ResourceAdmin,
    ResourceFile,
    ResourceFileAdmin,
    ResourceImage,
    ResourceImageAdmin,
    ResourceLink,
    ResourceLinkAdmin,
)


# Register your models here.
admin.site.register(Country, CountryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(TalkRoom, TalkRoomAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(SpeakerPerTalk, SpeakerPerTalkAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(SponsorLevel, SponsorLevelAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(StaticPage, StaticPageAdmin)

# polymorphic
admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceFile, ResourceFileAdmin)
admin.site.register(ResourceImage, ResourceImageAdmin)
admin.site.register(ResourceLink, ResourceLinkAdmin)
