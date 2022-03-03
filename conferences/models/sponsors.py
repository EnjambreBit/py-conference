from django.db import models
from sorl.thumbnail import ImageField


class Sponsor(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    logo = ImageField(upload_to="sponsors/logos/", default=None, blank=True, null=True)
    sponsor_level = models.ForeignKey(
        "SponsorLevel", related_name="sponsors", on_delete=models.CASCADE
    )
    confirmed = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "sponsors"
        verbose_name = "Sponsor"
        verbose_name_plural = "sponsors"

    def __str__(self):
        return f"{self.name} - {self.sponsor_level}"
