from operator import mod
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    timezone = models.CharField(max_length=100, default="Europe/London", blank=True, null=True)
    start_date = models.DateField(default=None, null=True, blank=True)
    end_date = models.DateField(default=None, null=True, blank=True)
    call_for_talks_start = models.DateField(default=None, null=True, blank=True)
    call_for_talks_end = models.DateField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'events'
        verbose_name = "Event"
        verbose_name_plural = "events"

    def __str__(self):
        return self.name
