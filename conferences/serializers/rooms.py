from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from conferences.models.rooms import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "id",
            "name",
        )

