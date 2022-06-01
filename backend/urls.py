from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
import backend.settings as settings
from django.views.generic.base import RedirectView


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("conferences.urls")),
    path("", include("pages.urls")),
]

if (
    settings.ENVIRONMENT == "DEVELOPMENT"
):  # en produccion los archivos estaticos son servido por nginx
    # urlpatterns = urlpatterns + [url(r'^assets/(?P<path>.*)$', RedirectView.as_view(url=settings.STATIC_URL + 'dist/assets/%(path)s', permanent=True), name='cloud-static'),]
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
