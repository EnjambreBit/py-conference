from conferences.models.profiles import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = "__all__"
        fields = [
            "first_name",
            "last_name",
            "nickname",
            "gender",
            "phone",
            "country",
            "document_type",
            "document_number",
            "birth_date",
            "company",
            "job_title",
            "institution_name",
            "study_program",
            "student_id",
        ]

        labels = {
            "first_name": "Nombres",
            "last_name": "Apellido",
            "nickname": "Apodo/Alias",
            "gender": "Genero",
            "phone": "Telefono",
            "country": "País",
            "document_type": "Tipo de documento",
            "document_number": "Número de documento",
            "birth_date": "Fecha de nacimiento",
            "company": "Empresa",
            "job_title": "Profesión",
            "institution_name": "Universidad/Institución",
            "study_program": "Carrera",
            "student_id": "Identificación Estudiantil",
        }
