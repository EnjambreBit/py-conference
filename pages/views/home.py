from conferences.models.events import Event
from conferences.models.speakers import Speaker
from django.views.generic import TemplateView
from conferences.models.speakers_per_talk import SpeakerPerTalk

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = Event.objects.filter(active=True).first()
        context["event"] = event

        #keynotes
        speakers_ids = [
            sp.speaker.id
            for sp in SpeakerPerTalk.objects.filter(
                talk__event=event, talk__status="published"
            )
        ]
        speakers = Speaker.objects.filter(id__in=speakers_ids)
        keynotes = [(s, s.weight(event)) for s in speakers if s.type(event) == "keynote"]
        keynotes.sort(key=lambda tup: tup[1], reverse=True) 
        keynotes = [s[0] for s in keynotes]
        context["keynotes"] = keynotes

        speakers = [(s, s.weight(event)) for s in speakers if s.type(event) != "keynote"]
        speakers.sort(key=lambda tup: tup[1], reverse=True) 
        speakers = [s[0] for s in speakers]
        context["speakers"] = speakers

        return context
