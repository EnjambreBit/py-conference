from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from conferences.models.countries import Country


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = (
            "id",
            "name",
            "alpha_2",
            "alpha_3",
        )
