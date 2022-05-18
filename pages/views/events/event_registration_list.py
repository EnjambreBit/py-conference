from django.views.generic import ListView
from conferences.models.events import Event


class EventRegistrationListView(ListView):
    model = Event
    template_name = "event/available-events.html"

    def get_queryset(self):
        return Event.objects.filter(active=True).order_by("-start_date")
