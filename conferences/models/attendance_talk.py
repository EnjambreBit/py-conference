from django.db import models


class AttendanceTalk(models.Model):
    profile = models.ForeignKey("Profile", related_name="attendance_talks", on_delete=models.CASCADE)
    talk_room = models.ForeignKey("TalkRoom", related_name="attendance_talks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'attendance_talk'
        verbose_name = "Attendance at the talk"
        verbose_name_plural = "Attendance at the talk"

    def __str__(self):
        return f"{self.profile} {self.talk_room}"
