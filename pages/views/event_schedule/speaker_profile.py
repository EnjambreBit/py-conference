from django.views.generic import DetailView
from conferences.models.speakers import Speaker
from conferences.models.talks import Talk


class SpeakerProfileView(DetailView):
    model = Speaker
    template_name = "event-schedule/speaker_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        talks = [
            spt.talk
            for spt in profile.speakers_per_talk.all()
            if spt.talk.status == "published"
        ]
        context["talks"] = talks
        return context
