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
    filterset_fields = ("__all__")

    # # 封装所有get函数
    # def __dim_query(self, request):
    #     re_dict = {'queryType': request.GET['queryType'], 'dd': 'saf'}
    #     return re_dict
    #
    # def get(self, request):
    #     # 查询bf
    #     if self.__dim_query(request)['queryType'] == 'bf':
    #         query_result = BeforeMatch.objects.all()
    #         query_result = BeforeMatchSer(query_result, many=True)
    #         filter_backends = (filters.DjangoFilterBackend,)
    #         filterset_class = BeforeMatchFil
    #         return Response(query_result.data)
    #     elif request.GET['queryType'] == 'rt':
    #         pass
    #     # 查询result
    #     else:
    #         pass
