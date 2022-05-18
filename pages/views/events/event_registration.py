from django.views.generic import DetailView
from conferences.models.events import Event
from django.contrib.auth.mixins import LoginRequiredMixin

# from conferences.models.events import Event
from conferences.models.event_registrations import EventRegistration
from conferences.models.profiles import Profile


class EventRegistrationView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "event/event-registration.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventRegistrationView, self).get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated:
            user_profile, _ = Profile.objects.get_or_create(user=self.request.user)
            event_registration, _ = EventRegistration.objects.get_or_create(event=self.object, profile=user_profile)
            context["event_registration"] = event_registration
            context["profile"] = user_profile
        return context
