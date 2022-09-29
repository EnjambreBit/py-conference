from django.contrib import admin
from conferences.models.talk_registration import TalkRegistration
from import_export.admin import ExportMixin
from import_export import resources
from import_export.fields import Field
from import_export.formats import base_formats
from conferences.filters.dropdown_filter import RelatedDropdownFilter


class TalkRegistrationResource(resources.ModelResource):
    name = Field(attribute="talk__name", column_name="Taller")
    first_name = Field(attribute="profile__first_name", column_name="Nombre")
    last_name = Field(attribute="profile__last_name", column_name="Apellido")
    document_type = Field(
        attribute="profile__document_type", column_name="Tipo de documento"
    )
    document_number = Field(
        attribute="profile__document_number", column_name="Número de documento"
    )

    class Meta:
        model = TalkRegistration
        fields = (
            "id",
            "name",
            "first_name",
            "last_name",
            "profile__user__email",
            "document_type",
            "document_number",
        )
        export_order = (
            "id",
            "last_name",
            "first_name",
            "document_type",
            "document_number",
            "profile__user__email",
            "name",
        )


class TalkRegistrationAdmin(ExportMixin, admin.ModelAdmin):
    model = TalkRegistration
    resource_class = TalkRegistrationResource
    list_display = (
        "id",
        "get_first_name",
        "get_last_name",
        "get_document_type",
        "get_document_number",
        "get_talk_name",
    )
    search_fields = ("talk", "profile")
    list_filter = (("talk", RelatedDropdownFilter),)

    def get_first_name(self, obj):
        return obj.profile.first_name

    get_first_name.short_description = "Nombre"

    def get_last_name(self, obj):
        return obj.profile.last_name

    get_last_name.short_description = "Apellido"

    def get_document_type(self, obj):
        return obj.profile.document_type

    get_document_type.short_description = "Tipo Documento"

    def get_document_number(self, obj):
        return obj.profile.document_number or "-"

    get_document_number.short_description = "Nro Documento"

    def get_talk_name(self, obj):
        return obj.talk.name

    get_talk_name.short_description = "Charla/Taller"
