from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

# from rest_framework_json_api.relations import ResourceRelatedField

from conferences.models.event_links import EventLink


class EventLinkSerializer(ModelSerializer):
    class Meta:
        model = EventLink
        fields = (
            "id",
            "nombre",
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
