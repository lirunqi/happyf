from django.urls import path
from .views import Query
from .views import handle_wx

urlpatterns = [
    path("", Query.as_view()),
    path("wechat",handle_wx)
]
