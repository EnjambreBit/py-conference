from django import forms
from conferences.models.resources import ResourceFile, ResourceLink, ResourceImage


class ResourceLinkForm(forms.ModelForm):
    class Meta:
        model = ResourceLink
        fields = [
            "talk",
            "title",
            "url",
        ]
        labels = {
            "title": "Titulo",
            "url": "Url",
        }


class ResourceImageForm(forms.ModelForm):
    pass


class ResourceFileForm(forms.ModelForm):
    pass
