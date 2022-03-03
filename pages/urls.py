from operator import index
from django.urls import path
from django.conf.urls import include, url

from pages.views.home import home_page
from pages.views.static_page import render_static_page
from pages.views.registration import profile_register

# Create your views here.
urlpatterns = [
    path("register", profile_register),
    path("pages/<slug:slug>/", render_static_page),
    path("", home_page, name="home"),
]
