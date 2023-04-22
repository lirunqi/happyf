from django.urls import path
from .views import DmView,DmCreateView

urlpatterns = [
    path('',DmView.as_view()),
    # path('form',DmFormView.as_view()),
    path('formadd',DmCreateView.as_view()),
]