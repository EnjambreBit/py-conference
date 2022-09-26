from django.views.generic import TemplateView
from conferences.models.talk_rooms import TalkRoom
from conferences.models.events import Event
import datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone


def talk_room_to_data(talk_room):
    lat, lng = talk_room.room.get_lat_lng()
    return {
        "id": talk_room.talk.id,
        "name": talk_room.talk.name,
        "type": talk_room.talk.get_talk_type_display(),
        "room": talk_room.room.name,
        "speakers": talk_room.talk.speakers(),
        "gmap_link": f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
    }

class TalkScheduleView(TemplateView):
    template_name = "event-schedule/talk_schedule.html"

    def get_context_data(self, **kwargs):
        event = Event.objects.filter(active=True).first()
        queryset = TalkRoom.objects.filter(talk__event=event)

        #dias del evento
        date = event.start_date
        days = [date]
        while date < event.end_date:
            date += relativedelta(days=1)
            days.append(date)
        active_date = kwargs.get("date", False)
        if not active_date:
            active_date = event.start_date.strftime("%Y-%m-%d")
        else:
            active_date = active_date.date()

        queryset = TalkRoom.objects.filter(date=active_date)

        #charlas
        start = queryset.first().start
        data = []
        hour_data = { 
            "start": start.strftime("%H:%M"),
            "off": if_ended(active_date, start), 
            "talks_room": [] 
        } 
        for talk_room in queryset:
            if talk_room.start:
                if talk_room.start > start:
                    data.append(hour_data)
                    start = talk_room.start
                    hour_data = { 
                        "start": talk_room.start.strftime("%H:%M"), 
                        "off": if_ended(active_date, talk_room.start),
                        "talks_room": [
                            talk_room_to_data(talk_room)
                        ] 
                    } 
                else:
                    hour_data["talks_room"].append(talk_room_to_data(talk_room))

        data.append(hour_data) 

        context = super().get_context_data(**kwargs)
        context["event"] = event
        context["talks"] = data
        context["days"] = days
        context["active_date"] = active_date
        return context


def if_ended(date, start):
    now = datetime.datetime.now()
    if isinstance(date, str):
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    current = datetime.datetime.combine(date, start) + relativedelta(hours=1)
    if now > current:
        return True
    return False



