from django.contrib.auth.mixins import AccessMixin
from conferences.models.speakers_per_talk import SpeakerPerTalk


class TalkOwnerRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission(request)

        talk = self.get_object()
        is_owner = (
            talk.speakers_per_talk.filter(
                speaker__profile=self.request.user.profile
            ).count()
            != 0
        )
        
        if talk is not None and is_owner or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        return self.handle_no_permission()
