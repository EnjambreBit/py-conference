from django.db import models


class EventRegistration(models.Model):
    event = models.ForeignKey(
        "Event",
        related_name="registrations",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )
    profile = models.ForeignKey(
        "Profile", related_name="registrations", on_delete=models.CASCADE
    )

    is_speaker = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)
    asked_for_a_grant = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "event_registrations"
        verbose_name = "Event Registration"
        verbose_name_plural = "Events Registrations"

    def __str__(self):
        return self.event.name
