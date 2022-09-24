from django.db import models


class Talk(models.Model):
    TALKS_TYPE = (
        ("talk", "Charla"),
        ("workshop", "Workshop/Taller"),
        # ("tutorial", "Tutorial"),
        ("keynote", "Keynote/Charla magistral"),
        ("lightning_talk", "Lightning Talk"),
        ("sprints", "Sprints"),
        ("open_space", "Open Space"),
        ("panel", "Panel"),
        # ("other", "Other"),
    )

    STATUS = (
        ("draft", "draft"),
        ("in_review", "in_review"),
        ("published", "published"),
        ("rejected", "rejected"),
    )

    LANGUAGES = (
        ("english", "Inglés"),
        ("spanish", "Español"),
        ("portuguese", "Portugues"),
        ("english/spanish", "Inglés/Español"),
    )

    AUDIENCE_LEVEL = (
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("all", "All"),
    )

    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    event = models.ForeignKey(
        "Event",
        related_name="talks",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )
    status = models.CharField(max_length=20, choices=STATUS, default="draft")
    talk_type = models.CharField(
        max_length=30, choices=TALKS_TYPE, default=None, blank=True, null=True
    )
    audience_level = models.CharField(
        max_length=30, choices=AUDIENCE_LEVEL, default=None, blank=True, null=True
    )
    language = models.CharField(
        max_length=30, default=None, choices=LANGUAGES, blank=True, null=True
    )
    language_slider = models.CharField(
        max_length=30, default=None, choices=LANGUAGES, blank=True, null=True
    )
    duration = models.IntegerField(
        "Duration in minutes", default=0, blank=True, null=True
    )
    summary = models.TextField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    topics = models.TextField(default=None, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "talks"
        verbose_name = "Talk"
        verbose_name_plural = "talks"

    def __str__(self):
        if self.status != "published":
            return f"({self.status}) - {self.name}"
        return f"{self.name}"

    def is_keynote(self):
        return self.talk_type == "keynote"

    def is_workshop(self):
        return self.talk_type == "workshop"

    def registration_required(self):
        return self.talk_type in ["workshop", "sprints"]

    @property
    def published(self):
        return self.status == "published"

    def weight(self):
        weights = {
            "keynote": 50,
            "sprints": 30,
            "workshop": 20,
            "talk": 10,
        }
        return weights.get(self.talk_type, 0)
    
    def speakers(self):
        speakers =[spp.speaker.profile.full_name for spp in self.speakers_per_talk.all()]
        return ", ".join(speakers)
