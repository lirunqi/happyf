from django.urls import path
from .views import Query
from .views import handle_wx
# from .views import handle_ai

urlpatterns = [
    path("", Query.as_view()),
    path("wechat",handle_wx),
    # path("ai",handel_ai)
]
