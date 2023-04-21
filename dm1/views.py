from django.shortcuts import render
from django.views.generic import ListView,FormView
from .models import Dm
from .form import DmForm

# Create your views here.
class DmView(ListView):
    model = Dm
    template_name = 'dm1/dm_list2.html'


class DmFormView(FormView):
    form_class = DmForm
    template_name = 'dm1/dm_form.html'

