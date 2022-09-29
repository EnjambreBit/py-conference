from django import template
from qr_code.qrcode.utils import (
    MeCard,
    VCard,
    EpcData,
    VEvent,
    EventClass,
    EventTransparency,
    EventStatus,
    WifiConfig,
    Coordinates,
    QRCodeOptions,
)
import datetime
from conferences.models.talk_rooms import TalkRoom

register = template.Library()


@register.inclusion_tag("tags/talk-preview.html")
def talk_preview(talk, hidden_resources=False):
    event = None
    room = TalkRoom.objects.filter(talk=talk).first()
    if room is not None and room.start is not None and room.end is not None:
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

    context = {"talk": talk, "have_resources": False, "event": event}
    if not hidden_resources:
        context["resources"] = talk.resources.all()
        context["have_resources"] = talk.resources.all().count() > 0

    return context
