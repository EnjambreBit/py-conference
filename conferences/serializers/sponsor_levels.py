from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from conferences.models.sponsor_levels import SponsorLevel


class SponsorLevelSerializer(ModelSerializer):
    class Meta:
        model = SponsorLevel
        fields = (
            "id",
            "name",
        )
