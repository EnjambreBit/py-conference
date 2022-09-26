import datetime
from conferences.models.events import Event
from conferences.models.talk_registration import TalkRegistration
from conferences.models.talk_rooms import TalkRoom
from conferences.models.talks import Talk
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import FormView, TemplateView
from pages.forms.workshop_attendance import WorkshopAttendanceForm
from django.urls import reverse_lazy
from dateutil.relativedelta import relativedelta


class WorkshopAttendanceView(FormView):
    template_name = "event-schedule/workshop-attendance.html"
    form_class = WorkshopAttendanceForm

    def get(self, request, *args, **kwargs):
        if not self.take_attendance():
            return HttpResponseRedirect(reverse_lazy("talks-schedule"))

        now = timezone.now()
        print("xxx", now)

        date_now = now.date()
        time_now = now.time()

        talk_id = self.kwargs.get("talk_id", None)
        talk_rooms = TalkRoom.objects.filter(talk__id=talk_id, date=date_now).order_by("end")
        talk_room = None
        if talk_rooms.count() == 0:
            return HttpResponseRedirect(reverse_lazy("talks-schedule"))

        elif talk_rooms.count() == 1:
            talk_room = talk_rooms.first()
        
        else:
            #talks_room = [tr for tr in talk_rooms]
            for tr in talk_rooms:
                end = datetime.datetime.combine(tr.date, tr.end) + relativedelta(minutes=30)
                end = end.time()
                if time_now < end:
                    talk_room = tr
                    break

        attendees = TalkRegistration.objects.filter(talk__id=talk_id)

        context_data = self.get_context_data()
        context_data["talk_room"] = talk_room
        context_data["attendees"] = attendees

        return self.render_to_response(context_data)

    def take_attendance(self):
        if self.request.user.is_authenticated:
            groups = list(self.request.user.groups.values_list('name', flat=True))
            if "Colaboradores" in groups:
                return True
        return False