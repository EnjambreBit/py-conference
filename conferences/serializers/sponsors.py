from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
# from rest_framework_json_api.relations import ResourceRelatedField

from conferences.models.sponsors import Sponsor


class SponsorSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = (
            'id',
            'name',
        )
