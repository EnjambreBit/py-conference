from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
# from rest_framework_json_api.relations import ResourceRelatedField

from conferences.models.speakers_per_talk import SpeakerPerTalk


class SpeakerPerTalkSerializer(ModelSerializer):
    class Meta:
        model = SpeakerPerTalk
        fields = (
            'id',
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
