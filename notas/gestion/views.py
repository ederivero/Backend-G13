from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

# utilizar las variables de nuestro archivo settings.py
from django.conf import settings

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
        # request.user > mostrara el usuario que esta autenticado (Usuario model)
        print(request.user.nombre)
        usuarioLogeado: Usuario = request.user
        print('----')
        # request.auth > mostrara la token que se esta utilizando para la autenticacion
        print(request.auth)
        
        if serializador.is_valid():
            nuevaNota = Nota(usuario= usuarioLogeado, **serializador.validated_data)
            nuevaNota.save()

            if nuevaNota.imagen:
                subir_imagen_s3('{}/media/{}'.format(settings.BASE_DIR, nuevaNota.imagen))

            return Response(data={
                'message':'Nota creada exitosamente'
            }, status=201)
        else:
            return Response(data={
                'message': 'Error al crear la nota',
                'content': serializador.errors
            }, status=400)

    def get(self, request):
        # TODO: implementar el listar todas las notas con sus items si es que tiene
        pass


@api_view(['GET'])
def devolverUrlImagen(request:Request, nombre_imagen):
    url = devolver_url_firmada(nombre_imagen)

    return Response(data={
        'url': url
    })


from boto3 import session
from os import environ,path

def subir_imagen_s3(nombre_imagen):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
    if nombre_imagen is None:
        return
    
    nuevaSesion = session.Session(
            aws_access_key_id=environ.get('AWS_ACCESS_KEY'), 
            aws_secret_access_key=environ.get('AWS_SECRET_KEY'), 
            region_name=environ.get('AWS_BUCKET_REGION'))
    
    s3Client = nuevaSesion.client('s3')

    bucket = environ.get('AWS_BUCKET_NAME')
    with open(nombre_imagen, 'rb') as archivo:
        object_name = path.basename(archivo.name) # nombre del archivo y si no se especifica entonces se usara el nombre original

        try:
            respuesta = s3Client.upload_file(nombre_imagen, bucket, object_name)
            print(respuesta)
        except Exception as e:
            print(e)


def devolver_url_firmada(nombre_imagen):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
    if nombre_imagen is None:
        return
    
    nuevaSesion = session.Session(
            aws_access_key_id=environ.get('AWS_ACCESS_KEY'), 
            aws_secret_access_key=environ.get('AWS_SECRET_KEY'), 
            region_name=environ.get('AWS_BUCKET_REGION'))
    bucket = environ.get('AWS_BUCKET_NAME')
    s3Client = nuevaSesion.client('s3')

    url = s3Client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': nombre_imagen}, ExpiresIn = 60)

    return url