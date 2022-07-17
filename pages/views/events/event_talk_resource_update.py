from django.views.generic import UpdateView
from django.urls import reverse_lazy
from conferences.models.resources import Resource
from conferences.models.talks import Talk

class EventTalkResourceUpdateView(UpdateView):
    template_name = "event/event-talk-resource-form.html"
    model = Resource
    success_url = reverse_lazy("talk_preview")

    # def get(self, request, pk, *args, **kwargs):
    #     context_data = self.get_context_data()
    #     talk = Talk.objects.get(pk=pk)
    #     context_data["talk"] = talk

    def get_form_class(self):
        component = self.get_object()

    def get_success_url(self):
        return reverse_lazy("talk_preview", kwargs={"pk": self.get_object().id})