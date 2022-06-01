from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from conferences.models.profiles import Profile
from my_addons.forms_widgets import CustomDateInputWidget

class AccountRegistrationForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    nickname = forms.CharField(max_length=100, required=False)
    gender = forms.ChoiceField(choices=Profile.GENDERS)

    document_type = forms.ChoiceField(choices=Profile.DOCUMENTS_TYPE)
    document_number = forms.CharField(max_length=100)
    birth_date = forms.DateField(widget=CustomDateInputWidget())
    company = forms.CharField(max_length=100, required=False)
    job_title = forms.CharField(max_length=100, required=False)
    institution_name = forms.CharField(max_length=100, required=False)
    study_program = forms.CharField(max_length=100, required=False)
    student_id = forms.CharField(max_length=50, required=False)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email
