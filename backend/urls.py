from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
    path("api/", include("conferences.urls")),
    path("", include("pages.urls")),
]
