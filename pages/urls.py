from operator import index
from django.urls import path
from django.conf.urls import include, url

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from pages.views.home import HomePageView
from pages.views.static_page import render_static_page

# from pages.views.registration import profile_register
from pages.views.event_cronogram import event_cronogram_page
from pages.views.location import location_page
from pages.views.accounts.account_profile_detail import ProfileDetailView
from pages.views.accounts.account_registration import AccountRegistrationView
from pages.views.not_implemented import NotImplementedView
from pages.views.events.event_registration_list import EventRegistrationListView
from pages.views.events.event_registration import EventRegistrationView
from pages.views.sponsors import SponsorListView


# Create your views here.
urlpatterns = [
    path("accounts/profile/", ProfileDetailView.as_view(), name="profile"),
    path("accounts/registration/", AccountRegistrationView.as_view(), name="registration"),
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
    path("location", location_page, name="location"),
    path("cronogram", event_cronogram_page, name="cronogram"),

    path("sponsors", SponsorListView.as_view(), name="sponsors"),
    
    path("pages/<slug:slug>/", render_static_page, name="page"),
    path("", HomePageView.as_view(), name="home"),
]
