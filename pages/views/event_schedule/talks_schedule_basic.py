from django.views.generic import TemplateView
from conferences.models.events import Event
from conferences.models.talks import Talk


class EventTalksScheduleBasicPageView(TemplateView):
    template_name = "event-schedule/talks_schedule_basic.html"

    def get_context_data(self, **kwargs):
        event_id = kwargs.get("pk", False)
        if event_id:
            event = Event.objects.get(id=event_id)
        else:
            event = Event.objects.filter(active=True).first()

        talks = [ (t, t.weight()) for t in self.get_queryset(event)]
        talks.sort(key=lambda tup: tup[1], reverse=True) 
        talks = [t[0] for t in talks]

        #el usuario logueado puede tomar asistencia
        take_attendance = False
        groups = self.request.user.groups.values_list('name', flat=True)
        if "Colaboradores" in groups:
            take_attendance = True

        context = super().get_context_data(**kwargs)
        context["event"] = event
        context["talks"] = talks
        context["not_talks"] = len(talks) == 0
        context["take_attendance"] = take_attendance
        return context

    def get_queryset(self, event):
        queryset = Talk.objects.filter(event=event, status="published")
        return queryset
