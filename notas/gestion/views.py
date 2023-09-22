from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


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


@api_view(['POST'])
def login(request: Request):
    serializador = LoginSerializer(data=request.data)

    if serializador.is_valid():
        usuarioEncontrado = Usuario.objects.filter(
            correo=serializador.validated_data.get('correo')).first()

        if not usuarioEncontrado:
            return Response(data={
                'message': 'El usuario no existe'
            }, status=400)

        # check_password > valida si es la password o no
        validacion_password = usuarioEncontrado.check_password(
            serializador.validated_data.get('password'))

        if validacion_password == False:
            return Response(data={
                'message': 'Credenciales invalidas'
            }, status=400)

        token = AccessToken.for_user(usuarioEncontrado)

        return Response(data={
            'content': str(token)
        })

    else:
        return Response(data={
            'message': 'Error al hacer el login',
            'content': serializador.errors
        })


class NotaController(APIView):
    # sirve para indicar que tipos de autenticacion vamos a manejar
    # AllowAny > permitir que cualquier persona identificada o no puedan consultar estos metodos
    # IsAuthenticated > solamente las personas que esten identificadas pueden consultar estos metodos
    # IsAuthenticatedOrReadOnly > solamente los metodos de lectura (GET, OPTIONS) podran ser consultados sin autenticacion mientras que los demas metodos la autenticacion es obligatoria
    # IsAdminUser > Valida que el usuario autenticado sea is_superuser (administrador) si no lo es no se le permitira acceder a los metodos
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        print('paso')
        serializador = NotaSerializer(data=request.data)

        if serializador.is_valid():
            pass
        else:
            return Response(data={
                'message': 'Error al crear la nota',
                'content': serializador.errors
            }, status=400)

    def get(self, request):
        pass
