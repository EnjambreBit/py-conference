from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
# from rest_framework_json_api.relations import ResourceRelatedField

from conferences.models.sponsor_levels import SponsorLevel


class SponsorLevelSerializer(ModelSerializer):
    class Meta:
        model = SponsorLevel
        fields = (
            'id',
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
