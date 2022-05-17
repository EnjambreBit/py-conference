from django.http import HttpResponse
from django.template import loader
from conferences.models.events import Event
from pages.forms.event_registration import EventRegistrationForm
from django.contrib.auth.models import User




def profile_register(request):
    template = loader.get_template("event-registration.html")
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            


            template = loader.get_template("event-registration-susccessful.html")

    else:
        form = EventRegistrationForm()
    
    context = {
        "event": Event.objects.filter(active=True).first(),
        "form": form,
    }

    return HttpResponse(template.render(context, request))
