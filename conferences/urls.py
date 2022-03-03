from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers

# from rest_framework.authtoken.views import obtain_auth_token

from conferences.views.countries import CountryViewSet
from conferences.views.events import EventViewSet
from conferences.views.rooms import RoomViewSet
from conferences.views.talks import TalkViewSet
from conferences.views.profiles import ProfileViewSet
from conferences.views.contact_information import ContactInformationViewSet
from conferences.views.speakers import SpeakerViewSet
from conferences.views.speakers_per_talk import SpeakerPerTalkViewSet
from conferences.views.sponsors import SponsorViewSet
from conferences.views.sponsor_levels import SponsorLevelViewSet
from conferences.views.static_pages import StaticPageViewSet
from conferences.views.grants import GrantViewSet
from conferences.views.talk_rooms import TalkRoomViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register("contact-information", ContactInformationViewSet)
router.register("countries", CountryViewSet)
router.register("events", EventViewSet)
router.register("grants", GrantViewSet)
router.register("profiles", ProfileViewSet)
router.register("rooms", RoomViewSet)
router.register("speakers", SpeakerViewSet)
router.register("speakers-per-talk", SpeakerPerTalkViewSet)
router.register("sponsors", SponsorViewSet)
router.register("sponsor-levels", SponsorLevelViewSet)
router.register("static-pages", StaticPageViewSet)
router.register("talks", TalkViewSet)
router.register("talk-rooms", TalkRoomViewSet)

urlpatterns = router.urls
