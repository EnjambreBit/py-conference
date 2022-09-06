from django.views.generic import TemplateView
from conferences.models.events import Event
from conferences.models.talks import Talk


class EventTalksCronogramBasicPageView(TemplateView):
    template_name = "cronogram/talks_cronogram_basic.html"

    def get_context_data(self, **kwargs):
        event_id = kwargs.get("pk", False)
        if event_id:
            event = Event.objects.get(id=event_id)
        else:
            event = Event.objects.filter(active=True).first()

        talks = [ (t, t.weight()) for t in self.get_queryset(event)]
        talks.sort(key=lambda tup: tup[1], reverse=True) 
        talks = [t[0] for t in talks]

        context = super().get_context_data(**kwargs)
        context["event"] = event
        context["talks"] = talks
        context["not_talks"] = len(talks) == 0
        return context

    def get_queryset(self, event):
        queryset = Talk.objects.filter(event=event, status="published")
        return queryset
