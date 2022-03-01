from unicodedata import name
from django.db import models


class Resource(models.Model):
    RESOURCE_TYPE = (
        ("file", "File"),
        ("link", "Link"),
    )
    talk = models.ForeignKey("Talk", related_name="resources", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=10, choices=RESOURCE_TYPE, default="File")
    url = models.CharField(max_length=200, default=None, blank=True, null=True)
    file = models.FileField(upload_to="resources/", default=None, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "resources"
        verbose_name = "Resource"
        verbose_name_plural = "resources"

    def __str__(self):
        return f"{self.talk} - {self.type}"
