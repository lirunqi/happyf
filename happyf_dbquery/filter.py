from django_filters import rest_framework as filters
from .models import *


class BeforeMatchFil(filters.FilterSet):
    class Meta:
        model = BeforeMatch
        fields = "__all__"
