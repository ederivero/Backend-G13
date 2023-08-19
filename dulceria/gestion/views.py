from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import CategoriaModel
from .serializers import CategoriaSerializer
from rest_framework import status


# ejemplo de como renderizar plantillas
def paginaInicio(request):
    print(request)
    data = {
        'usuario': {
            'nombre': 'Eduardo',
            'apellido': 'De Rivero'
        },
        'hobbies': [
            {
                'descripcion': 'Ir al cine'
            },
            {
                'descripcion': 'Ir a la piscina'
            }
        ]
    }

    return render(request, 'inicio.html', {'data': data})


@api_view(http_method_names=['GET', 'POST'])
def devolverHoraServidor(request: Request):
    print(request.method)

    if request.method == 'GET':

        return Response(data={
            'content': datetime.now()
        })
    elif request.method == 'POST':
        return Response(data={
            'content': 'Para saber la hora, realiza un GET'
        })


class CategoriasController(APIView):
    def get(self, request: Request):
        # SELECT * FROM categorias;
        categorias = CategoriaModel.objects.all()
        print(categorias)

        return Response(data={
            'message': 'La categoria es`'
        })

    def post(self, request: Request):
        # donde se guarda la info proveniente del cliente
        data = request.data
        # data > validar la info entrante y ver que cumpla con los parametros necesarios
        serializador = CategoriaSerializer(data=data)

        validacion = serializador.is_valid()
        if validacion == True:
            nuevaCategoria = serializador.save()
            print(nuevaCategoria)

            return Response(data={
                'message': 'Categoria creada exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al crear la categoria',
                'content': serializador.errors  # me da un listado con los errores
            }, status=status.HTTP_400_BAD_REQUEST)
