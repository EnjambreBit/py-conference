import datetime
from conferences.models.talk_rooms import TalkRoom
from conferences.models.talks import Talk
from django.http import HttpResponse
from qr_code.qrcode.utils import EventClass, EventStatus, EventTransparency, VEvent


def download_talk_ics_file(request, pk):
    room = TalkRoom.objects.filter(talk__id=pk).first()
    if room is not None:
        talk = room.talk
        talk_start = datetime.datetime.combine(room.date, room.start)
        talk_end = datetime.datetime.combine(room.date, room.end)
        event = VEvent(
            uid=talk.pk,
            summary=talk.name,
            start=talk_start,
            end=talk_end,
            location=f"Universidad de salta, Salta, Argentina - {room.room.name}",
            geo=room.room.get_lat_lng(),
            categories=["SciPy"],
            status=EventStatus.CONFIRMED,
            event_class=EventClass.PUBLIC,
            transparency=EventTransparency.OPAQUE,
            # organizer="foo@bar.com",
            # url="https://bar.com",
            description=talk.summary[:200],
        )

        response = HttpResponse(event.make_qr_code_data(), content_type="text/calendar")
        response["Content-Disposition"] = f"attachment; filename=charla.ics"
        return response

    else:
        HttpResponse("Page not found", status=404)
