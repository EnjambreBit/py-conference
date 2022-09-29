from django.views.generic import TemplateView
from conferences.models.events import Event
from conferences.models.speakers_per_talk import SpeakerPerTalk
from conferences.models.speakers import Speaker


class EventSpeakersPageView(TemplateView):
    template_name = "event-schedule/speakers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = Event.objects.filter(active=True).first()

        speakers_ids = [
            sp.speaker.id
            for sp in SpeakerPerTalk.objects.filter(
                talk__event=event, talk__status="published"
            )
        ]
        speakers = Speaker.objects.filter(id__in=speakers_ids)
        speakers = [(s, s.weight(event)) for s in speakers]
        speakers.sort(key=lambda tup: tup[1], reverse=True)
        speakers = [s[0] for s in speakers]

        context["event"] = event
        context["speakers"] = speakers
        context["not_speakers"] = len(speakers) == 0

        return context
