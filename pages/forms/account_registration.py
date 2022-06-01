from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from conferences.models.profiles import Profile


class AccountRegistrationForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    nickname = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=Profile.GENDERS)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email
