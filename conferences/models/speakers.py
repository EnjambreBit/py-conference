import profile
from statistics import mode
from django.db import models
from sorl.thumbnail import ImageField
from django.apps import apps as django_apps


class Speaker(models.Model):
    profile = models.OneToOneField(
        "Profile", related_name="speaker", on_delete=models.CASCADE
    )
    photo = ImageField(
        upload_to="speakers/photos/", default=None, blank=True, null=True
    )
    biography = models.TextField(default=None, blank=True, null=True)
    sort_weight = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "speakers"
        verbose_name = "Speaker"
        verbose_name_plural = "speakers"

    def __str__(self):
        return self.profile.full_name

    def weight(self, event=None):
        weight = 0
        if event is None:
            Event = django_apps.get_model("conferences.Event")
            event = Event.objects.filter(active=True).first()

        for spt in self.speakers_per_talk.filter(
            talk__event=event, talk__status="published"
        ):
            if spt.talk.weight() > weight:
                weight = spt.talk.weight()
        return weight + self.sort_weight

    def type(self, event=None):
        talks_weights = {
            "keynote": 50,
            "sprints": 30,
            "workshop": 20,
            "talk": 10,
        }
        if event is None:
            Event = django_apps.get_model("conferences.Event")
            event = Event.objects.filter(active=True).first()

        talks_weights = {v: k for k, v in talks_weights.items()}
        weight = self.weight(event) - self.sort_weight
        return talks_weights.get(weight, None)
