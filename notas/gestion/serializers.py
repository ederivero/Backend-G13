from rest_framework import serializers
from .models import *


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    correo = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        # fields = '__all__'
        exclude = ['usuario']
