from conferences.models.events import Event
from conferences.models.profiles import Profile
from conferences.models.speakers import Speaker
from conferences.models.speakers_per_talk import SpeakerPerTalk
from conferences.models.talks import Talk
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic.base import TemplateView


class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = None
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            pass

        context["profile"] = profile

        #evento actual activo
        now = timezone.now()
        event: Event = Event.objects.filter(active=True, call_for_talks_start__gte=now, call_for_talks_end__lte=now).first()
        context["event"] = event

        if profile is not None:
            context["registrations"] = profile.registrations.all()
            context["talk_registrations"] = profile.talks_registrations_profile.all()

            speaker_profile = Speaker.objects.filter(profile=profile).first()

            if speaker_profile:
                tids = [
                    spt.talk.id
                    for spt in SpeakerPerTalk.objects.filter(speaker=speaker_profile)
                ]
                talks = Talk.objects.filter(id__in=tids)
                context["talks"] = talks
                context["is_speaker"] = True

        return context
