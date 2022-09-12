from conferences.models.events import Event
from django.views.generic import TemplateView


class AgendaPageView(TemplateView):
    template_name = "agenda/agenda.html"

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context["events"] = Event.objects.filter(active=True).first()
    #    return context
