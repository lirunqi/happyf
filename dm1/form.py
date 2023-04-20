from django import forms


class dm(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField(max_value=1000)
    sex = forms.CharField(max_length=3)
    email = forms.EmailField()
