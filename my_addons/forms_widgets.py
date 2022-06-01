from django import forms


class CustomDateInputWidget(forms.DateInput):
    input_type = 'date'