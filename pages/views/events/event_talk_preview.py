from urllib import request
from django.views.generic import DetailView
from conferences.models.talks import Talk
from django.utils import timezone


class TalkPreviewView(DetailView):
    model = Talk
    template_name = "event/event-talk-preview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        talk = self.get_object()
        now = timezone.now().date()
        if now <= talk.event.end_date:
            context["can_edit"] = talk.speakers_per_talk.filter(
                speaker__profile=self.request.user.profile
            ).count() > 0 or self.request.user.is_superuser

        return context
