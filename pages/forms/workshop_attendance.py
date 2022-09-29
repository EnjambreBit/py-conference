from django import forms


class WorkshopAttendanceForm(forms.Form):
    profile = forms.IntegerField(required=False)
    talk_room = forms.IntegerField(required=False)
