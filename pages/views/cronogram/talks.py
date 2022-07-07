from django.views.generic import TemplateView
from conferences.models.events import Event
from conferences.models.talks import Talk


class EventTalksPageView(TemplateView):
    template_name = "cronogram/talks.html"

    def get_context_data(self, **kwargs):
        event_id = kwargs.get("pk", False)
        if event_id:
            event = Event.objects.get(id=event_id)
        else:
            event = Event.objects.filter(active=True).first()

        talks = Talk.objects.filter(event=event, status="published")

        context = super().get_context_data(**kwargs)
        context["event"] = event
        context["talks"] = talks
        context["not_talks"] = talks.count() == 0
        return context
