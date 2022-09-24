import datetime
from conferences.models.events import Event
from conferences.models.talk_rooms import TalkRoom
from conferences.models.talks import Talk
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView, TemplateView
from pages.forms.workshop_attendance import WorkshopAttendanceForm


class WorkshopAttendanceView(FormView):
    template_name = "event-schedule/workshop-attendance.html"
    form_class = WorkshopAttendanceForm

    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now().date()
        #talk_room = TalkRoom.objects.filter(talk__id=talk_id)
        
        context_data = self.get_context_data()

        return self.render_to_response(context_data)

