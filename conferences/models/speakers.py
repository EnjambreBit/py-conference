import profile
from django.db import models
from sorl.thumbnail import ImageField


class Speaker(models.Model):
    profile = models.OneToOneField(
        "Profile", related_name="speaker", on_delete=models.CASCADE
    )
    photo = ImageField(
        upload_to="speakers/photos/", default=None, blank=True, null=True
    )
    biography = models.TextField(default=None, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "speakers"
        verbose_name = "Speaker"
        verbose_name_plural = "speakers"

    def __str__(self):
        return self.profile.full_name

    def weight(self, event):
        weight = 0
        for spt in self.speakers_per_talk.filter(talk__event=event):
            if spt.talk.weight() > weight:
                weight = spt.talk.weight()
        return weight