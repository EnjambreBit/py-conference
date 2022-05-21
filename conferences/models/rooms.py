from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    internal_name = models.CharField(
        max_length=200, default=None, blank=True, null=True
    )
    capacity = models.IntegerField(default=0, blank=True, null=True)

    address = models.OneToOneField("Address", on_delete=models.CASCADE, related_name="room", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "rooms"
        verbose_name = "Room"
        verbose_name_plural = "rooms"

    def __str__(self):
        return self.name
