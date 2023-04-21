from django.urls import path
from .views import DmView,DmFormView

urlpatterns = [
    path('',DmView.as_view()),
    path('from',DmFormView.as_view())
]