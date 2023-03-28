from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .serializers import *
from .models import *
from .filter import *
from wechatpy.utils import check_signature
from django.conf import settings
from django.http import HttpResponse


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

def handle_wx(request):
    if request.method == 'GET':
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echo_str = request.GET.get('echostr', '')
        check_signature(settings.TOKEN, signature, timestamp, nonce)

        response = HttpResponse(echo_str, content_type="text/plain")
        return response




class AiAna:
    '''
    通过Post请求接收a,b两个参数，再将a b 两个参数传给aiquery.py里面的函数获取返回值，最终返回给调用方
    '''
    pass
