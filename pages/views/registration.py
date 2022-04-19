from django.http import HttpResponse
from django.template import loader
from conferences.models.events import Event
from pages.forms.event_registration import EventRegistrationForm


def profile_register(request):
    template = loader.get_template("event-registration.html")
    form = EventRegistrationForm()
    context = {
        "event": Event.objects.filter(active=True).first(),
        "form": form,
    }
    return HttpResponse(template.render(context, request))
