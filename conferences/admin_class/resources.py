from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter,
)
from conferences.models.resources import (
    Resource,
    ResourceFile,
    ResourceImage,
    ResourceLink,
)


class ResourceAdmin(PolymorphicParentModelAdmin):
    base_model = Resource
    list_display = (
        "id",
        "talk",
        "type",
        "title",
    )
    child_models = (ResourceFile, ResourceImage, ResourceLink)


class ResourceFileAdmin(PolymorphicChildModelAdmin):
    base_model = ResourceFile
    list_display = (
        "id",
        "talk",
        "title",
        "file",
    )


class ResourceImageAdmin(PolymorphicChildModelAdmin):
    base_model = ResourceImage
    list_display = (
        "id",
        "talk",
        "title",
        "photo",
    )


class ResourceLinkAdmin(PolymorphicChildModelAdmin):
    base_model = ResourceLink
    list_display = (
        "id",
        "talk",
        "title",
        "url",
    )
