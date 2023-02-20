from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .serializers import *
from .models import *
from .filter import *

# Create your views here.
'''
bf_query
rt_query
result_query
'''


class Query(generics.ListAPIView):
    queryset = BeforeMatch.objects.all()
    serializer_class = BeforeMatchSer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = "__all__"


class Data_Provider:
    def __init__(self):
        data_set = []
    pass


class Data_Minner:
    pass
