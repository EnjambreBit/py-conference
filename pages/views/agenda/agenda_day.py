from ast import Import
from datetime import date
from conferences.models.events import Event
from django.views.generic import TemplateView, FormView
from django.http import HttpRequest, HttpResponse
from pages.forms.agenda_day import AgendaDayForm
from conferences.models.talks import Talk
from conferences.models.talk_rooms import TalkRoom
from conferences.models.rooms import Room
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


class AgendaDayPageView(FormView):
    template_name = "agenda/agenda_day.html"
    form_class = AgendaDayForm


    def get(self, request, day=0,*args, **kwargs):
        talks = None
        fecha = None
        room = request.GET.get('room',0)
        if day != 0:
            fecha = date(2022, 9, day)
        if fecha and room != 0:
            talks = TalkRoom.objects.filter(talk__event__pk=3, date=fecha, room__pk=room).order_by('start')
            
        else:
            talks = None
        rooms = Room.objects.all()
        context_data = self.get_context_data()
        context_data["talks"] = talks
        context_data["rooms"] = rooms

        return self.render_to_response(context_data)

    # def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    #    self.room = request.POST['room']
    #    return super().post(request, *args, **kwargs)

    # def form_invalid(self, form) -> HttpResponse:
    #    return super().form_invalid(form)


    def form_valid(self, form):
        self.room = form.cleaned_data['room']
        url = reverse(
                "talks-agenda-day",
                kwargs={
                    "day": self.kwargs.get('day'),
                })
        return HttpResponseRedirect(f"{url}?room={form.cleaned_data['room']}")


#     #def get_context_data(self, **kwargs):
#     #    context = super().get_context_data(**kwargs)
#     #    context["events"] = Event.objects.filter(active=True).first()
#     #    return context
