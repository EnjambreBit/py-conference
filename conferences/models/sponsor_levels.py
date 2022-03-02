from operator import mod
from django.db import models


class SponsorLevel(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    priority = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sponsor_levels'
        verbose_name = "Sponsor level"
        verbose_name_plural = "Sponsor levels"
        ordering = ["-priority"]

    def __str__(self):
        return self.name

    def total(self):
        return self.sponsors.count()
