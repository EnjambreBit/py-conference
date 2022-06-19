from django.db import models


class EventLink(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name="event_links")
    url = models.URLField(max_length=200, default=None, blank=True, null=True)
    static_page = models.ForeignKey("StaticPage", on_delete=models.CASCADE, default=None, blank=True, null=True)
    order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'event_links'
        verbose_name = "EventLink"
        verbose_name_plural = "Event links"
        ordering = ['order']

    def __str__(self):
        return self.name
