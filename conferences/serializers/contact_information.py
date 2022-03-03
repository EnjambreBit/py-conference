from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from conferences.models.contact_information import ContactInformation


class ContactInformationSerializer(ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = (
            'id',
        )
