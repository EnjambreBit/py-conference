from rest_framework.serializers import ModelSerializer
from conferences.models.talk_registration import TalkRegistration


class TalkRegistrationSerializer(ModelSerializer):
    class Meta:
        model = TalkRegistration
        fields = '__all__'
