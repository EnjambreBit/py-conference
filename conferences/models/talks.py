from django.db import models


class Talk(models.Model):
    TALKS_TYPE = (
        ("talk", "Talk"),
        ("workshop", "Workshop"),
        ("tutorial", "Tutorial"),
        ("keynote", "Keynote"),
        ("lightning_talk", "Lightning Talk"),
        ("open_space", "Open Space"),
        ("panel", "Panel"),
        ("other", "Other"),
    )

    LANGUAGES = (
        ("english", "English"),
        ("spanish", "Spanish"),
        ("portuguese", "Portuguese"),
        ("english/spanish", "English/Spanish"),
    )

    AUDIENCE_LEVEL = (
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("all", "All"),
    )

    name = models.CharField(max_length=200, default=None, blank=True, null=True)
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
    published = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "talks"
        verbose_name = "Talk"
        verbose_name_plural = "talks"

    def __str__(self):
        return self.name
