from django.urls import path
from .views import Prueba, registrar
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('prueba', Prueba.as_view()),
    path('registro', registrar),
    path('login', TokenObtainPairView.as_view()),
]
