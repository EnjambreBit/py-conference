from django import forms



class AgendaDayForm(forms.Form):
    day = forms.IntegerField(required=False)
    room = forms.IntegerField(required=False)



