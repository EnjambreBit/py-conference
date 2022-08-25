from urllib import request
from django.views.generic import DetailView
from conferences.models.talks import Talk
from django.utils import timezone


class TalkDetailView(DetailView):
    model = Talk
    template_name = "cronogram/talk_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        talk = self.get_object()
        context["resources"] = talk.resources.all()
        return context
