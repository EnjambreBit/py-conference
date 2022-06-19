from django.views.generic import TemplateView
from conferences.models.events import Event
from conferences.models.speakers_per_talk import SpeakerPerTalk
from conferences.models.speakers import Speaker


class EventSpeakersPageView(TemplateView):
    template_name = "cronogram/speakers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = Event.objects.filter(active=True).first()
         
        speakers_ids = [sp.speaker.id for sp in SpeakerPerTalk.objects.filter(talk__event=event, talk__status="published")]
        speakers = Speaker.objects.filter(id__in=speakers_ids)
        context["event"] = event
        context["speakers"] = speakers

        return context
