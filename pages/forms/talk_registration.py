from django import forms
from conferences.models.talks import Talk



class TalkRegistrationForm(forms.ModelForm):
    use_required_attribute = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

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
        required = [
            'name',
            'talk_type',
            'audience_level',
            'language',
            'language_slider',
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
            "audience_level": "Nivel de audiencia",
            "language": "Idioma",
            "language_slider": "Idioma de las diapositivas",
        }