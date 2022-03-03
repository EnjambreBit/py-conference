from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from conferences.models.grants import Grant


class GrantSerializer(ModelSerializer):
    class Meta:
        model = Grant
        fields = ("id",)
