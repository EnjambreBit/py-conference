from django.views.generic import TemplateView
from conferences.models.events import Event
from conferences.models.talks import Talk


class EventTalksPageView(TemplateView):
    template_name = "event-schedule/talks.html"

    def get_context_data(self, **kwargs):
        event_id = kwargs.get("pk", False)
        if event_id:
            event = Event.objects.get(id=event_id)
        else:
            event = Event.objects.filter(active=True).first()

        talks = self.get_queryset(event)

        context = super().get_context_data(**kwargs)
        context["event"] = event
        context["talks"] = talks
        context["not_talks"] = talks.count() == 0
        return context

    def get_queryset(self, event):
        queryset = Talk.objects.filter(event=event, status="published")
        queryset = queryset.exclude(talk_type__in=["sprints", "workshop", "keynote"])
        return queryset


class EventSprintPageView(EventTalksPageView):
    template_name = "event-schedule/sprints.html"
    
    def get_queryset(self, event):
        queryset = Talk.objects.filter(event=event, talk_type="sprints", status="published")
        return queryset


class EventWorkshopPageView(EventTalksPageView):
    template_name = "event-schedule/workshops.html"

    def get_queryset(self, event):
        queryset = Talk.objects.filter(event=event, talk_type="workshop", status="published")
        return queryset


class EventKeynotePageView(EventTalksPageView):
    template_name = "event-schedule/keynotes.html"

    def get_queryset(self, event):
        queryset = Talk.objects.filter(event=event, talk_type="keynote", status="published")
        return queryset