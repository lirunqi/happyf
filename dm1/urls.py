from django.urls import path
from .views import dmView

urlpatterns = [
    path('',dmView.as_view()),
]