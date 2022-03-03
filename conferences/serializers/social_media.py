from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from conferences.models.social_media import SocialMedia


class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = (
            "id",
            "name",
        )
