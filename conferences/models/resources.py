from unicodedata import name
from django.db import models
from polymorphic.models import PolymorphicModel
from sorl.thumbnail import ImageField


class Resource(PolymorphicModel):
    talk = models.ForeignKey("Talk", related_name="resources", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "resources"
        verbose_name = "Resource"
        verbose_name_plural = "resources"

    def __str__(self):
        return f"{self.talk} - {self.type}"

    @property
    def type(self):
        return self.__class__.__name__


class ResourceFile(Resource):
    file = models.FileField(upload_to="resources/", default=None, blank=True, null=True)

class ResourceImage(Resource):
    photo = ImageField(upload_to="resources/", default=None, blank=True, null=True)

class ResourceLink(Resource):
    url = models.CharField(max_length=200, default=None, blank=True, null=True)


