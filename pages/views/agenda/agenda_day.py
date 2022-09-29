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

    def get(self, request, day, *args, **kwargs):
        event = Event.objects.filter(active=True).first()
        queryset = TalkRoom.objects.filter(talk__event=event)

        room_id = request.GET.get("room", False)

        if room_id:
            queryset = queryset.filter(room__id=room_id)

        if day:
            date_ = date(2022, 9, day)
            queryset = queryset.filter(date=date_)
            queryset = queryset.order_by("start")

        else:
            queryset = []

        context_data = self.get_context_data()
        context_data["talks"] = queryset
        context_data["rooms"] = Room.objects.all()
        context_data["room_id"] = room_id

        return self.render_to_response(context_data)

    # def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    #    self.room = request.POST['room']
    #    return super().post(request, *args, **kwargs)

    # def form_invalid(self, form) -> HttpResponse:
    #    return super().form_invalid(form)

    def form_valid(self, form):
        self.room = form.cleaned_data["room"]
        url = reverse_lazy(
            "talks-agenda-day",
            kwargs={
                "day": self.kwargs.get("day"),
            },
        )
        return HttpResponseRedirect(f"{url}?room={form.cleaned_data['room']}")


#     #def get_context_data(self, **kwargs):
#     #    context = super().get_context_data(**kwargs)
#     #    context["events"] = Event.objects.filter(active=True).first()
#     #    return context
