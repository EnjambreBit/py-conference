from operator import mod
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    description = models.TextField(default=None, null=True, blank=True)
    timezone = models.CharField(
        max_length=100, default="Europe/London", blank=True, null=True
    )
    start_date = models.DateField(default=None, null=True, blank=True)
    end_date = models.DateField(default=None, null=True, blank=True)
    # call for talks
    call_for_talks_start = models.DateField(default=None, null=True, blank=True)
    call_for_talks_end = models.DateField(default=None, null=True, blank=True)
    # registration
    registration_start = models.DateField(default=None, null=True, blank=True)
    registration_end = models.DateField(default=None, null=True, blank=True)

    registration_url = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    registration_enabled = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    address = models.ForeignKey("Address", on_delete=models.CASCADE, related_name="event", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "events"
        verbose_name = "Event"
        verbose_name_plural = "events"

    def __str__(self):
        return self.name

    def registered_menbers(self):
        return self.registrations.count()
