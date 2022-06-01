from conferences.models.events import Event
from django.views.generic import TemplateView


class LocationPageView(TemplateView):
    template_name = "location.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = Event.objects.filter(active=True).first()
        return context
