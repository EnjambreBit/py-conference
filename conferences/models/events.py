from django.db import models
from django.utils import timezone


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
    registration_enabled = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    address = models.ForeignKey(
        "Address",
        on_delete=models.CASCADE,
        related_name="events",
        null=True,
        blank=True,
    )

    call_for_papers_page = models.ForeignKey(
        "StaticPage",
        related_name="events_cfp_page",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    location_content = models.ForeignKey(
        "StaticPage",
        related_name="events_location",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    code_of_conduct_page = models.ForeignKey(
        "StaticPage",
        related_name="events_code_of_conduct",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    data_manipulation_page = models.ForeignKey(
        "StaticPage",
        related_name="events_data_manipulation",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

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

    def call_for_talks_active(self):
        now = timezone.now().date()
        if now >= self.call_for_talks_start and now <= self.call_for_talks_end:
            return True
        return False
