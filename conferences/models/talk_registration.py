import profile
from django.db import models


class TalkRegistration(models.Model):
    talk = models.ForeignKey(
        "Talk", related_name="talks_registrations", on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        "Profile", related_name="talks_registrations_profile", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "talk_registrations"
        verbose_name = "Talk Registration"
        verbose_name_plural = "Talk Registrations"

    def __str__(self):
        return f"{self.talk} - {self.profile.full_name}"
