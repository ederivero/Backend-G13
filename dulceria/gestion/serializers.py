# https://www.django-rest-framework.org/api-guide/serializers/
from rest_framework import serializers
from .models import CategoriaModel


class CategoriaSerializer(serializers.ModelSerializer):
    # basarme en un modelo para que haga todas las validaciones correspondientes
    class Meta:
        model = CategoriaModel
        # si utilizar absolutamente todos los atributos del modelo entonces usa la sgte forma
        fields = '__all__'
        # fields = ['id', 'nombre', 'nivelAzucar']
        # si quieres utilizar todos los atributos menos uno o la minoria
        # exclude = ['id']
        # NOTA: o se usa el atributo fields o el atributo exclude pero no los dos al mismo tiempo
