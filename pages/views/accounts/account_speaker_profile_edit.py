from django.views.generic import UpdateView
from django.urls import reverse_lazy
from conferences.models.speakers import Speaker
from pages.forms.speaker import SpeakerForm


class SpeakeProfileUpdateView(UpdateView):
    template_name = "account/account_speaker_profile_edit.html"
    model = Speaker
    form_class = SpeakerForm

    def get_object(self, queryset=None):
        user = self.request.user
        speaker = user.profile.speaker
        if speaker is None:
            speaker = Speaker.objects.crete(profile=user.profile)
        return speaker

    def get_success_url(self):
        return reverse_lazy("profile")
