from django.urls import path
from .views import Prueba, registrar, login, NotaController
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('prueba', Prueba.as_view()),
    path('registro', registrar),
    path('login', TokenObtainPairView.as_view()),
    path('login-custom', login),
    path('notas', NotaController.as_view())
]
