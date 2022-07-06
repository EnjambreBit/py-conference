from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from conferences.models.profiles import Profile
from my_addons.forms_widgets import CustomDateInputWidget



class AccountRegistrationForm(forms.Form):
    use_required_attribute = False

    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Contraseña", max_length=100, widget=forms.PasswordInput())
    first_name = forms.CharField(label="Nombres", max_length=100)
    last_name = forms.CharField(label="Apellido", max_length=100)
    phone = forms.CharField(label="Telefono", max_length=100)
    nickname = forms.CharField(label="Apodo/Alias", max_length=100, required=False)
    gender = forms.ChoiceField(label="Genero", choices=Profile.GENDERS)

    document_type = forms.ChoiceField(label="Tipo de documento", choices=Profile.DOCUMENTS_TYPE, required=False)
    document_number = forms.CharField(label="Número de documento", max_length=100, required=False)
    birth_date = forms.DateField(label="Fecha de nacimiento", widget=CustomDateInputWidget(), required=False)
    company = forms.CharField(label="Empresa", max_length=100, required=False)
    job_title = forms.CharField(label="Profesión", max_length=100, required=False)
    institution_name = forms.CharField(label="Universidad/Institución", max_length=100, required=False)
    study_program = forms.CharField(label="Carrera", max_length=100, required=False)
    student_id = forms.CharField(label="Identificación Estudiantil", max_length=50, required=False)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Ya existe un usuario registrado con este email.")
        return email
