from gc import get_objects
from django.views.generic import UpdateView

from conferences.models.talks import Talk
from pages.forms.talk_registration import TalkRegistrationForm
from conferences.models.talks import Talk
from my_addons.mixins import TalkOwnerRequiredMixin
from django.urls import reverse_lazy


class EventTalkUpdateView(TalkOwnerRequiredMixin, UpdateView):
    template_name = "event/event-talk-registration.html"
    model = Talk
    form_class = TalkRegistrationForm
    success_url = reverse_lazy("talk_preview")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = self.get_object().event
        context["edition"] = True
        return context

    def get_success_url(self):
        return reverse_lazy("talk_preview", kwargs={"pk": self.get_object().id})
