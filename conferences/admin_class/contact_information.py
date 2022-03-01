from django.contrib import admin
from conferences.models.contact_information import ContactInformation


class ContactInformationAdmin(admin.ModelAdmin):
    model = ContactInformation
    list_display = (
        'id',
        'profile',
    )

