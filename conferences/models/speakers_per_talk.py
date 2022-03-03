from django.db import models


class SpeakerPerTalk(models.Model):
    talk = models.ForeignKey("Talk", related_name="speakers_per_talk", on_delete=models.CASCADE)
    speaker = models.ForeignKey("Speaker", related_name="speakers_per_talk", on_delete=models.CASCADE)
    speaker_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'speakers_per_talk'
        verbose_name = "Speaker per talk"
        verbose_name_plural = "speakers per talk"

    def __str__(self):
         return f"{self.speaker} - {self.talk}" 
