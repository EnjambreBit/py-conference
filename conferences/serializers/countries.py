from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

# from rest_framework_json_api.relations import ResourceRelatedField

from conferences.models.countries import Country


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = (
            "id",
            "nombre",
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
