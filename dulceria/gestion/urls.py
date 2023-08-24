# aca declararemos todas las rutas pertenecientes a esta aplicacion
from django.urls import path
# cuando colocamos '.' indicamos que se trata de un archivo en el mismo nivel, sin embargo si no colocamos el '.' estaremos indicando que sera o una libreria o un archivo externo
from .views import (paginaInicio,
                    devolverHoraServidor,
                    CategoriasController,
                    CategoriaController,
                    GolosinasController)

urlpatterns = [
    path('inicio', paginaInicio),
    path('status', devolverHoraServidor),
    path('categorias', CategoriasController.as_view()),
    path('categoria/<id>', CategoriaController.as_view()),
    path('golosinas', GolosinasController.as_view())
]
