from django.db import models


class Resource(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'resources'
        verbose_name = "Resource"
        verbose_name_plural = "resources"

    def __str__(self):
        return self.name
