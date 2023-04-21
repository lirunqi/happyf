from django.urls import path
from .views import DmView,DmFormView,DmFormaddView

urlpatterns = [
    path('',DmView.as_view()),
    path('form',DmFormView.as_view()),
    path('formadd',DmFormaddView.as_view()),
]