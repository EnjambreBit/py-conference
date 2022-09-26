from django.views.generic import DeleteView
from conferences.models.resources import Resource
from django.urls import reverse_lazy


class EventTalkResourceDeleteView(DeleteView):
    template_name = "event/event-talk-resource-delete.html"
    model = Resource

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["talk"] = self.get_object().talk
        return context_data

    def get_success_url(self):
        return reverse_lazy("talk_preview", kwargs={"pk": self.get_object().talk.id})
