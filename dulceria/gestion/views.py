from math import ceil
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import CategoriaModel, GolosinaModel
from .serializers import CategoriaSerializer, GolosinaSerializer
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
        serializador = CategoriaSerializer(instance=categorias, many=True)

        return Response(data={
            'message': 'La categoria es`',
            'content': serializador.data
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


class CategoriaController(APIView):
    def get(self, request: Request, id: str):
        categoriaEncontrada = CategoriaModel.objects.filter(id=id).first()
        if not categoriaEncontrada:
            return Response(data={
                'message': 'Categoria no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = CategoriaSerializer(instance=categoriaEncontrada)
        return Response(data={
            'content': serializador.data
        })

    def put(self, request: Request, id: str):
        categoriaEncontrada = CategoriaModel.objects.filter(id=id).first()
        if not categoriaEncontrada:
            return Response(data={
                'message': 'Categoria no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializador = CategoriaSerializer(data=data)
        dataValida = serializador.is_valid()
        if dataValida:
            serializador.validated_data  # la data convertida a un diccionario con los campos que necesita el modelo, si se le llegase a pasar algun campo que no utiliza este automaticamente no se guardaria en este atributo
            serializador.update(categoriaEncontrada,
                                serializador.validated_data)

            return Response(data={
                'message': 'Categoria actualizada exitosamente'
            })

        else:
            return Response(data={
                'message': 'Error al actualizar la categoria',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: str):
        categoriaEncontrada = CategoriaModel.objects.filter(id=id).first()
        if not categoriaEncontrada:
            return Response(data={
                'message': 'Categoria no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)

        CategoriaModel.objects.filter(id=id).delete()

        return Response(data={
            'message': 'Categoria eliminada exitosamente'
        })


class GolosinasController(APIView):
    def get(self, request: Request):
        # page = request.query_params.get('page') if request.query_params.get('page') is not None else 1
        page = int(request.query_params.get('page', 1))
        # perPage = request.query_params.get('page') if request.query_params.get('page') is not None else 5
        perPage = int(request.query_params.get('perPage', 5))

        ordering = request.query_params.get('ordering')
        orderingType = request.query_params.get('orderingType')  # asc | desc
        orderingType = '' if orderingType == 'asc' else '-'

        # OPERADOR TERNARIO
        # VALOR_VERDADERO if CONDICION else VALOR_FALSO
        # numero = 5
        # total = 100 if numero > 10 else 200

        # cuantos elementos me voy a saltar
        # si queremos que primero se realice la suma o resta colocar entre parentesis para luego segun el nivel proceda con la operacion externa a los parentesis
        skip = (page - 1) * perPage
        # cuantos elementos vas a tomar
        take = perPage * page

        if ordering:
            golosinas = GolosinaModel.objects.order_by(ordering).all()[
                skip:take]
        else:
            golosinas = GolosinaModel.objects.all()[skip:take]

        totalGolosinas = GolosinaModel.objects.count()

        serializador = GolosinaSerializer(instance=golosinas, many=True)

        pagination = helperPagination(totalGolosinas, page, perPage)

        return Response(data={
            'content': serializador.data,
            'pagination': pagination
        })


def helperPagination(total: int, page: int, perPage: int):
    itemsPerPage = perPage if total >= perPage else total
    totalPages = ceil(total / itemsPerPage) if itemsPerPage > 0 else None
    prevPage = page - 1 if page > 1 and page <= totalPages else None
    nextPage = page + 1 if totalPages > 1 and page < totalPages else None

    return {
        'itemsPerPage': itemsPerPage,
        'totalPages': totalPages,
        'prevPage': prevPage,
        'nextPage': nextPage
    }
