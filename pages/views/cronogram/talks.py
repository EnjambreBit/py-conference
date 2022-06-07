from django.views.generic import TemplateView
from conferences.models.events import Event
from conferences.models.speakers_per_talk import SpeakerPerTalk
from conferences.models.speakers import Speaker


class EventTalksPageView(TemplateView):
    template_name = "talks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = Event.objects.filter(active=True).first()
        context["event"] = event        
        return context


