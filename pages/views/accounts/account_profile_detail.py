from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from conferences.models.profiles import Profile
from conferences.models.speakers import Speaker
from conferences.models.speakers_per_talk import SpeakerPerTalk
from conferences.models.talks import Talk


class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            profile = Profile.objects.get(user=self.request.user)

        except Profile.DoesNotExist:
            context["profile"] = None

        if profile is not None:
            context["profile"] = profile
            context["registrations"] = profile.registrations.all()

            speaker_profile = Speaker.objects.filter(profile=profile).first()

            if speaker_profile:
                tids = [spt.talk.id for spt in SpeakerPerTalk.objects.filter(speaker=speaker_profile)]
                talks = Talk.objects.filter(id__in=tids)
                context["talks"] = talks
                context["is_speaker"] = True

        return context
