from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from conferences.models.speakers_per_talk import SpeakerPerTalk


class SpeakerPerTalkSerializer(ModelSerializer):
    class Meta:
        model = SpeakerPerTalk
        fields = ("id",)
