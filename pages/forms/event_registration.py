from django import forms


class EventRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    nickname = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(EventRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"