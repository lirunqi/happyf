from django.urls import path
from .views import *
from .views import handle_wx
# from .views import handle_ai

urlpatterns = [
    path("", Query.as_view()),
    path("wechat",handle_wx),
    path("get/",Query.as_view()),
    path("predict/",TestftView.as_view()),
    path("ttest/",TestftView.as_view()),

]
