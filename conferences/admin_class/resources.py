from django.contrib import admin
from conferences.models.resources import Resource


class ResourceAdmin(admin.ModelAdmin):
    model = Resource
    list_display = ("id",)
