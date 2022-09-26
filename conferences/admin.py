from django.contrib import admin

from conferences.admin_class.addresses import Address, AddressAdmin
from conferences.admin_class.attendance_talk import (AttendanceTalk,
                                                     AttendanceTalkAdmin)
from conferences.admin_class.contact_information import (
    ContactInformation, ContactInformationAdmin)
from conferences.admin_class.countries import Country, CountryAdmin
from conferences.admin_class.event_links import EventLink, EventLinkAdmin
from conferences.admin_class.event_registrations import (
    EventRegistration, EventRegistrationAdmin)
from conferences.admin_class.events import Event, EventAdmin
from conferences.admin_class.grants import Grant, GrantAdmin
from conferences.admin_class.profiles import Profile, ProfileAdmin
from conferences.admin_class.resources import (Resource, ResourceAdmin,
                                               ResourceFile, ResourceFileAdmin,
                                               ResourceImage,
                                               ResourceImageAdmin,
                                               ResourceLink, ResourceLinkAdmin)
from conferences.admin_class.rooms import Room, RoomAdmin
from conferences.admin_class.social_media import SocialMedia, SocialMediaAdmin
from conferences.admin_class.speakers import Speaker, SpeakerAdmin
from conferences.admin_class.speakers_per_talk import (SpeakerPerTalk,
                                                       SpeakerPerTalkAdmin)
from conferences.admin_class.sponsor_levels import (SponsorLevel,
                                                    SponsorLevelAdmin)
from conferences.admin_class.sponsors import Sponsor, SponsorAdmin
from conferences.admin_class.static_pages import StaticPage, StaticPageAdmin
from conferences.admin_class.talk_registration import (TalkRegistration,
                                                       TalkRegistrationAdmin)
from conferences.admin_class.talk_rooms import TalkRoom, TalkRoomAdmin
from conferences.admin_class.talks import Talk, TalkAdmin

# Register your models here.
admin.site.register(Country, CountryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(TalkRoom, TalkRoomAdmin)
admin.site.register(TalkRegistration, TalkRegistrationAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(SpeakerPerTalk, SpeakerPerTalkAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(SponsorLevel, SponsorLevelAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(StaticPage, StaticPageAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(EventLink, EventLinkAdmin)

# polymorphic
admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceFile, ResourceFileAdmin)
admin.site.register(ResourceImage, ResourceImageAdmin)
admin.site.register(ResourceLink, ResourceLinkAdmin)
admin.site.register(AttendanceTalk, AttendanceTalkAdmin)

