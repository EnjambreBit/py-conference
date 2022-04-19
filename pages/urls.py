from operator import index
from django.urls import path
from django.conf.urls import include, url

from pages.views.home import home_page
from pages.views.static_page import render_static_page
from pages.views.registration import profile_register
from pages.views.event_cronogram import event_cronogram_page
from pages.views.location import location_page
from pages.views.sponsors import sponsors_page

# Create your views here.
urlpatterns = [
    path("register", profile_register, name="register"),
    path("location", location_page, name="location"),
    path("cronogram", event_cronogram_page, name="cronogram"),
    path("sponsors", sponsors_page, name="sponsors"),
    path("pages/<slug:slug>/", render_static_page, name="page"),
    path("", home_page, name="home"),
]
