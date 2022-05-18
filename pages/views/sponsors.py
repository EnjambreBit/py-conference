from django.http import HttpResponse
from django.template import loader
from conferences.models.events import Event


def sponsors_page(request):
    template = loader.get_template("sponsors.html")
    context = {
        "event": Event.objects.filter(active=True).first(),
    }
    return HttpResponse(template.render(context, request))