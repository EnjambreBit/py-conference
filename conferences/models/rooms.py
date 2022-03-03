from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    internal_name = models.CharField(
        max_length=200, default=None, blank=True, null=True
    )
    capacity = models.IntegerField(default=0, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=10, decimal_places=7, default=None, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=10, decimal_places=7, default=None, blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "rooms"
        verbose_name = "Room"
        verbose_name_plural = "rooms"

    def __str__(self):
        return self.name
