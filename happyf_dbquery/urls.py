from django.urls import path
from .views import Query
from .views import handle_wx

urlpatterns = [
    path('', Query.as_view(), name='query'),
    path('wechat', handle_wx, name='wechat'),
    path('get/', Query.as_view(), name='get'),
]
