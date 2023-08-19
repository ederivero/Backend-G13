from django.db import models
from uuid import uuid4
# https://docs.djangoproject.com/en/4.2/topics/db/models/


class CategoriaModel(models.Model):
    opcionesNivelAzucar = (
        # si usaramos formularios dentro de django
        # bd , lo que mostraria en el formulario
        ['MA', 'MUY_ALTO'],
        ['ALTO', 'ALTO'],
        ['MEDIO', 'MEDIO'],
        ['BAJO', 'BAJO'],
        ['MUY_BAJO', 'MUY_BAJO'],
        ['CERO', 'CERO']
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.TextField(null=False)
    nivelAzucar = models.TextField(
        db_column='nivel_azucar', null=False, choices=opcionesNivelAzucar)

    class Meta:
        # https://docs.djangoproject.com/en/4.2/ref/models/options/
        db_table = 'categorias'


class GolosinaModel(models.Model):
    tipoProcedencia = (
        ['NACIONAL', 'NACIONAL'],
        ['IMPORTADO', 'IMPORTADO']
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.TextField(null=False)
    fechaVencimiento = models.DateField(
        editable=False, null=False, db_column='fecha_vencimiento')
    precio = models.FloatField(null=False)
    procedencia = models.TextField(choices=tipoProcedencia, default='NACIONAL')
    # relaciones
    # on_delete > cuando se elimine un registro de la categoria y esta tenga golosinas, como deberia actuar la base de datos? Sus opciones SON
    # CASCADE > eliminar la categoria y eliminar sus golosinas
    # PROTECT > evitar la eliminacion y lanzara un error de tipo ProtectedError
    # RESTRICT > evitara la eliminacion pero lanzara un error de tipo RestrictedError
    # SET_NULL > eliminar la categoria y en este cambio cambiar el id por null (NOTA: no se tiene que colocar null=False)
    # SET_DEFAULT > eliminara la categoria y cambiar el valor de sus golosinas a un valor por defecto
    # DO_NOTHING > no se debe utilizar esto, deja el id en esta columna a pesar que ya no exista por ende generara mala integridad de datos

    # related_name > crea un atributo virtual en mi otro modelo para poder acceder a todos sus golosinas desde la categoria, si no se define este parametro usara el siguiente formato NOMBRE_MODELO_set > GolosinaModel_set
    # internamente cuando se mande a llamar a este atributo generara un join entre las tablas de manera dinamica (no siempre se crea el join, solo cunado se llama)
    categoria = models.ForeignKey(
        to=CategoriaModel, db_column='categoria_id', on_delete=models.PROTECT, related_name='golosinas')

    class Meta:
        db_table = 'golosinas'
        # unicidad entre dos o mas columnas
        # jamas se podra repetir en un registro el nombre y la fechaVencimiento
        # constraint | restriccion
        # nombres de las COLUMNAS no de los atributos si usamos el parametro name
        # caso contrario usar el parametro del atributo
        unique_together = [['nombre', 'fechaVencimiento']]
