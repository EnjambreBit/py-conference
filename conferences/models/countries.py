from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    alpha_2 = models.CharField(max_length=2, default=None, blank=True, null=True)
    alpha_3 = models.CharField(max_length=3, default=None, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "countries"
        verbose_name = "Country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name
