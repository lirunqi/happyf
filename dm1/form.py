from django import forms


class DmForm(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField()
    sex = forms.CharField(max_length=3)