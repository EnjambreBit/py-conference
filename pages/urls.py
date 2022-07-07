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
from pages.views.cronogram.talks import EventTalksPageView
from pages.views.events.event_talk_registration import (
    EventTalkRegistrationView,
    EventTalkRegistrationSuccesfull,
)
from pages.views.playground import PlaygroundView
from pages.views.events.event_talk_preview import TalkPreviewView
from pages.views.events.event_talk_update import EventTalkUpdateView


# Create your views here.
urlpatterns = [
    path("accounts/profile/", ProfileDetailView.as_view(), name="profile"),
    path(
        "accounts/registration/", AccountRegistrationView.as_view(), name="registration"
    ),
    path("accounts/profile/edit/", NotImplementedView.as_view(), name="profile_edit"),
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
    path("talks/preview/<int:pk>/", TalkPreviewView.as_view(), name="talk_preview"),
    path("talks/edit/<int:pk>/", EventTalkUpdateView.as_view(), name="talk_edit"),
    path(
        "talks/edit/<int:pk>/upload-resource/",
        NotImplementedView.as_view(),
        name="talk_upload_resource",
    ),
    path("talks/<int:pk>/", EventTalksPageView.as_view(), name="event_talks"),
    path("location", LocationPageView.as_view(), name="location"),
    path("speakers", EventSpeakersPageView.as_view(), name="speakers"),
    path("sponsors", SponsorListView.as_view(), name="sponsors"),
    path("pages/<slug:slug>/", render_static_page, name="static_page"),
    path("playground/", PlaygroundView.as_view(), name="playground"),
    path("", HomePageView.as_view(), name="home"),
]
