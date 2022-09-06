from operator import index
from django.urls import path
from django.conf.urls import include, url

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from pages.views.home import HomePageView
from pages.views.static_page import render_static_page
from pages.views.location import LocationPageView
from pages.views.accounts.account_profile_detail import ProfileDetailView
from pages.views.accounts.account_registration import AccountRegistrationView
from pages.views.not_implemented import NotImplementedView
from pages.views.events.event_registration_list import EventRegistrationListView
from pages.views.events.event_registration import EventRegistrationView
from pages.views.sponsors import SponsorListView
from pages.views.cronogram.speakers import EventSpeakersPageView
from pages.views.cronogram.talks import EventTalksPageView, EventKeynotePageView, EventSprintPageView, EventWorkshopPageView
from pages.views.events.event_talk_registration import (
    EventTalkRegistrationView,
    EventTalkRegistrationSuccesfull,
)
from pages.views.playground import PlaygroundView
from pages.views.events.event_talk_preview import TalkPreviewView
from pages.views.events.event_talk_update import EventTalkUpdateView
from pages.views.events.event_talk_resource_create import TalkResourceCreateView
from pages.views.events.event_talk_resource_create_by_type import (
    TalkResourceCreateByTypeView,
)
from pages.views.events.event_talk_resource_update import EventTalkResourceUpdateView
from pages.views.events.event_talk_resource_delete import EventTalkResourceDeleteView
from pages.views.accounts.account_speaker_profile_edit import SpeakeProfileUpdateView
from pages.views.accounts.account_profile_edit import ProfileUpdateView
from pages.views.cronogram.speaker_profile import SpeakerProfileView
from pages.views.events.talk_registration import  TalkRegistration, TalkRegistrationAdd, TalkRegistrationDel
from pages.views.cronogram.talk_detail import TalkDetailView
from pages.views.twitter_news import TwitterNewsView
from pages.views.cronogram.talks_cronogram_basic import EventTalksCronogramBasicPageView


# Create your views here.
urlpatterns = [
    path("not-found/", NotImplementedView.as_view(), name="not_found"),
    path("accounts/profile/", ProfileDetailView.as_view(), name="profile"),
    path(
        "accounts/registration/", AccountRegistrationView.as_view(), name="registration"
    ),
    path("accounts/profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
    path("accounts/speaker/edit/", SpeakeProfileUpdateView.as_view(), name="speaker_profile_edit"),
    path(
        "accounts/change-password/",
        PasswordChangeView.as_view(template_name="account/change-password.html"),
        name="change_password",
    ),
    path(
        "accounts/change-password/done/",
        PasswordChangeDoneView.as_view(
            template_name="account/change-password-done.html"
        ),
        name="password_change_done",
    ),
    path(
        "events/availables",
        EventRegistrationListView.as_view(),
        name="available_events",
    ),
    path(
        "events/registration/<int:pk>/",
        EventRegistrationView.as_view(),
        name="event_registration",
    ),
    path(
        "events/<int:pk>/talks/talk-registration",
        EventTalkRegistrationView.as_view(),
        name="event-talk-registration",
    ),
    path(
        "events/talks/talk-registration-succesfull/<int:pk>/",
        EventTalkRegistrationSuccesfull.as_view(),
        name="event-talk-registration-succesfull",
    ),
    path("events/talks/", EventTalksPageView.as_view(), name="talks"),
    path("events/sprints/", EventSprintPageView.as_view(), name="sprints"),
    path("events/workshops/", EventWorkshopPageView.as_view(), name="workshops"),
    path("events/keynotes/", EventKeynotePageView.as_view(), name="keynotes"),
    path("event/talks/<int:pk>/", EventTalksPageView.as_view(), name="event_talks"),
    path("talks/detail/<int:pk>/", TalkDetailView.as_view(), name="talk_detail"),
    path("talks/preview/<int:pk>/", TalkPreviewView.as_view(), name="talk_preview"),
    path("talks/edit/<int:pk>/", EventTalkUpdateView.as_view(), name="talk_edit"),
    path(
        "talks/add-resource/<int:pk>/",
        TalkResourceCreateView.as_view(),
        name="talk_resource_type",
    ),
    path(
        "talks/add-resource/<int:pk>/<str:type>/",
        TalkResourceCreateByTypeView.as_view(),
        name="talk_resource_create",
    ),
    path(
        "talks/update-resource/<int:pk>/",
        EventTalkResourceUpdateView.as_view(),
        name="talk_resource_update",
    ),
    path(
        "talks/delete-resource/<int:pk>/",
        EventTalkResourceDeleteView.as_view(),
        name="talk_resource_delete",
    ),
    path("location", LocationPageView.as_view(), name="location"),
    path("noticias", TwitterNewsView.as_view(), name="twitter_news"),
    path("speakers", EventSpeakersPageView.as_view(), name="speakers"),
    path("speakers/<int:pk>/", SpeakerProfileView.as_view(), name="speaker_profile"),
    path("sponsors", SponsorListView.as_view(), name="sponsors"),
    path("pages/<slug:slug>/", render_static_page, name="static_page"),
    path("playground/", PlaygroundView.as_view(), name="playground"),
    path("talks/talk-registration/", TalkRegistration.as_view(), name="talk-registration"),
    path("talks/talk-registration/add/<int:pk>/", TalkRegistrationAdd, name="talk-registration-add"),
    path("talks/talk-registration/del/<int:pk>/", TalkRegistrationDel, name="talk-registration-del"),
    path("crongram/", EventTalksCronogramBasicPageView.as_view(), name="talks-cronogram"),
    path("", HomePageView.as_view(), name="home"),
]

