from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
# from rest_framework_json_api.relations import ResourceRelatedField

from conferences.models.rooms import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'id',
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
