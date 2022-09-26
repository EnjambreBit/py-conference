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
from conferences.models.profiles import Profile
from conferences.models.attendance_talk import AttendanceTalk



class WorkshopAttendanceView(TemplateView):
    template_name = "event-schedule/workshop-attendance.html"
    form_class = WorkshopAttendanceForm

    def get(self, request, *args, **kwargs):
        if not self.take_attendance():
            return HttpResponseRedirect(reverse_lazy("talks-schedule"))

        now = timezone.now()
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

        attendees = TalkRegistration.objects.filter(talk__id=talk_id).order_by("profile__first_name")

        confirmed_assistance = AttendanceTalk.objects.filter(talk_room=talk_room).values_list('profile__id', flat=True)
        print("::", confirmed_assistance)

        context_data = self.get_context_data()
        context_data["talk_room"] = talk_room
        context_data["attendees"] = attendees
        context_data["confirmed_assistance"] = confirmed_assistance

        return self.render_to_response(context_data)

    def take_attendance(self):
        if self.request.user.is_authenticated:
            groups = list(self.request.user.groups.values_list('name', flat=True))
            if "Colaboradores" in groups:
                return True
        return False


class UpdateAttendanceView(TemplateView):
    template_name = "event-schedule/talks_schedule_basic.html"

    def get(self, request, *args, **kwargs):
        if not self.take_attendance():
            return HttpResponseRedirect(reverse_lazy("talks-schedule"))

        talk_room_id = kwargs.get("talk_room_id", None)
        profile_id = kwargs.get("profile_id", None)

        try:
            profile = Profile.objects.get(id=profile_id)
            talk_room = TalkRoom.objects.get(id=talk_room_id)
            atendance, _created = AttendanceTalk.objects.get_or_create(talk_room=talk_room, profile=profile)
            if not _created:
                atendance.delete()

        except TalkRoom.DoesNotExist:
            return HttpResponseRedirect(reverse_lazy("talks-schedule"))

        except Profile.DoesNotExist:
            return HttpResponseRedirect(reverse_lazy("talks-schedule"))

        return HttpResponseRedirect(reverse_lazy("workshop-attendance", kwargs={"talk_id": talk_room.talk.id }))


    def take_attendance(self):
        if self.request.user.is_authenticated:
            groups = list(self.request.user.groups.values_list('name', flat=True))
            if "Colaboradores" in groups:
                return True
        return False