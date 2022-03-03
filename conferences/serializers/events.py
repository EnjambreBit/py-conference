from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from conferences.models.events import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "timezone",
            "start_date",
            "end_date",
            "call_for_talks_start",
            "call_for_talks_end",
            "registration_start",
            "registration_end",
        )
