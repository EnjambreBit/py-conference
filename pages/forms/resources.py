from django import forms
from conferences.models.resources import ResourceFile, ResourceLink, ResourceImage


class ResourceCreateForm(forms.Form):
    types = (
        ("link", "Link"),
        ("image", "Imagen"),
        ("file", "Archivo"),
    )

    resource_type = forms.ChoiceField(
        label="Tipo", choices=types, widget=forms.RadioSelect
    )

class ResourceLinkForm(forms.ModelForm):
    class Meta:
        model = ResourceLink
        fields = "__all__"
        labels = {
            "title": "Titulo",
            "url": "Url",
        }


class ResourceImageForm(forms.ModelForm):
    class Meta:
        model = ResourceImage
        fields = "__all__"
        labels = {
            "title": "Titulo",
            "photo": "Imagen",
        }


class ResourceFileForm(forms.ModelForm):
    class Meta:
        model = ResourceFile
        fields = "__all__"
        labels = {
            "title": "Titulo",
            "file": "Archivo",
        }
