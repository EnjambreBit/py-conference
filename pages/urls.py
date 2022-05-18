from operator import index
from django.urls import path
from django.conf.urls import include, url

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from pages.views.home import home_page
from pages.views.static_page import render_static_page

# from pages.views.registration import profile_register
from pages.views.event_cronogram import event_cronogram_page
from pages.views.location import location_page
from pages.views.sponsors import sponsors_page
from pages.views.accounts import ProfileView
from pages.views.not_implemented import NotImplementedView
from pages.views.events.event_registration_list import EventRegistrationListView
from pages.views.events.event_registration import EventRegistrationView


# Create your views here.
urlpatterns = [
    path("accounts/profile/", ProfileView.as_view(), name="profile"),
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
    path("sponsors", sponsors_page, name="sponsors"),
    path("pages/<slug:slug>/", render_static_page, name="page"),
    path("", home_page, name="home"),
]
