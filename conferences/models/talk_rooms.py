from django.db import models


class TalkRoom(models.Model):
    talk = models.ForeignKey("Talk", related_name="talks", on_delete=models.CASCADE)
    room = models.ForeignKey("Room", related_name="rooms", on_delete=models.CASCADE)
    date = models.DateField(default=None, null=True, blank=True)
    start = models.TimeField(default=None, null=True, blank=True)
    end = models.TimeField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "talk_rooms"
        verbose_name = "TalkRoom"
        verbose_name_plural = "Talk Rooms"

    # def __str__(self):
    #     return self.talk
