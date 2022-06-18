from django import forms
from conferences.models.talks import Talk



class TalkRegistrationForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = [
            "name",
            "event",
            "talk_type",
            "audience_level",
            "language",
            "language_slider",
            "summary",
            "topics",
            "description",
        ]
