from django import forms
from .models import Dm

class DmForm(forms.ModelForm):
    class Meta:
        model = Dm
        fields = ['name', 'age', 'sex']