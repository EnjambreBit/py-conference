from django.views.generic import FormView, DetailView
from django import forms
from pages.forms.talk_registration import TalkRegistrationForm
from conferences.models.events import Event
from conferences.models.speakers_per_talk import SpeakerPerTalk
from conferences.models.speakers import Speaker
from conferences.models.profiles import Profile
from conferences.models.talks import Talk
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect



class EventTalkRegistrationView(FormView):
    template_name = "event/event-talk-registration.html"
    form_class = TalkRegistrationForm
    success_url = reverse_lazy("event-talk-registration-succesfull")
    model = None

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['event'].widget = forms.HiddenInput()
        return form

    def get_initial(self):
        initial = super().get_initial()
        initial["event"] = self.kwargs["pk"]
        return initial

    def get(self, request, pk, *args, **kwargs):
        context_data = self.get_context_data()

        event = Event.objects.get(pk=pk)
        context_data["event"] = event

        return self.render_to_response(context_data)

    def form_valid(self, form):
        self.model = form.save()
        user_profile, _ = Profile.objects.get_or_create(user=self.request.user)
        speaker_profile, _ = Speaker.objects.get_or_create(profile=user_profile)
        SpeakerPerTalk.objects.create(talk=self.model, speaker=speaker_profile)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("event-talk-registration-succesfull", kwargs={'pk': self.model.id })


class EventTalkRegistrationSuccesfull(DetailView):
    template_name = "event/event-talk-registration-succesfull.html"
    model = Talk