from django.views.generic import UpdateView
from django.urls import reverse_lazy
from conferences.models.speakers import Speaker
from pages.forms.speaker import SpeakerForm


class EventTalkResourceUpdateView(UpdateView):
    template_name = "event/event-talk-resource-form.html"
    model = Speaker
    form_class = SpeakerForm