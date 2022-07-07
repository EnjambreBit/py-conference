from django.template.defaulttags import register
from django.utils.safestring import mark_safe
from conferences.models.events import Event


@register.inclusion_tag("tags/event-links.html")
def event_urls():
    urls = []
    event = Event.objects.filter(active=True).first()
    if event:
        urls = event.event_links.filter(active=True).order_by("order")
    return {"event": event, "urls": urls}
