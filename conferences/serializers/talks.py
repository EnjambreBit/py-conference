from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from conferences.models.talks import Talk


class TalkSerializer(ModelSerializer):
    class Meta:
        model = Talk
        fields = (
            "id",
            "name",
            "talk_type",
            "audience_level",
            "language",
            "language_slider",
            "duration",
            "summary",
            "description",
            "topics",
            "published",
        )
