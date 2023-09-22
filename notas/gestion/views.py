from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .serializers import *
from .models import *


class Prueba(APIView):

    def get(self, request):
        return Response(data={'message': 'hola'})


@api_view(['POST'])
def registrar(request: Request):
    serializador = RegistroSerializer(data=request.data)

    if serializador.is_valid():
        nuevoUsuario = Usuario(**serializador.validated_data)
        # metodo propio del modelo auth_user que me permite generar el hash de la password
        nuevoUsuario.set_password(serializador.validated_data.get('password'))

        nuevoUsuario.save()

        return Response(data={'message': 'Usuario registrado exitosamente'}, status=201)

    else:
        return Response(data={
            'message': 'Error al crear el usuario',
            'content': serializador.errors
        })
