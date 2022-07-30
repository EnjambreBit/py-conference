from conferences.models.speakers import Speaker
from django import forms


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = [
            "photo",
            "biography"
        ]