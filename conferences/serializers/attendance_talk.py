from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

# from rest_framework_json_api.relations import ResourceRelatedField

from conferences.models.attendance_talk import AttendanceTalk


class AttendanceTalkSerializer(ModelSerializer):
    class Meta:
        model = AttendanceTalk
        fields = ("id",)
