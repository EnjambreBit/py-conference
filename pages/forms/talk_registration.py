from django import forms
from conferences.models.talks import Talk



class TalkRegistrationForm(forms.ModelForm):
    use_required_attribute = False

    def __init__(self, *args, **kwargs):
        super(TalkRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['talk_type'].required = True
        self.fields['audience_level'].required = True
        self.fields['language'].required = True
        self.fields['language_slider'].required = True
        self.fields['summary'].required = True
        self.fields['topics'].required = True
        self.fields['description'].required = True

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
        labels = {
            "name": "Titulo de la propuesta",
            "talk_type": "Tipo",
            "summary": "Resumen / Abstract",
            "topics": "Palabras claves / Keywords",
            "description": "Descripcion Ampliada",
        }