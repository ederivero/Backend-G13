from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from uuid import uuid4
from phonenumber_field.modelfields import PhoneNumberField


class CategoriaModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    nombre = models.TextField(null=False, unique=True)
    # agarra la hora actual de la base de datos y lo pone en esta columna
    fechaCreacion = models.DateTimeField(
        auto_now_add=True, db_column='fecha_creacion')

    class Meta:
        db_table = 'categorias'


class VehiculoModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    # varchar(6)
    placa = models.CharField(max_length=6, unique=True, null=False)
    numeroSerie = models.TextField(unique=True, null=False, db_column='num_serie')
    color = models.TextField()
    puertas = models.IntegerField(null=False)
    peso = models.FloatField()
    dimensiones = models.JSONField()
    anioFabricacion = models.TextField(db_column='anio_fabricacion')
    categoria = models.ForeignKey(to=CategoriaModel, on_delete=models.PROTECT, db_column='categoria_id')
    class Meta:
        db_table = 'vehiculos'

class UsuarioModel(AbstractBaseUser):
    tipoUsuario = [('ADMINISTRADOR', 'ADMINISTRADOR'), ('CLIENTE', 'CLIENTE')]
    # voy a modificar de 0 mi tabla auth_user de la aplicacion auth
    id = models.UUIDField(default=uuid4, primary_key=True)
    nombre = models.TextField(null=False)
    apellido = models.TextField(null=False)
    correo = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    # auto_now_add > agarra la hora actual del servidor y la agrega al momento de hacer un nuevo registro (creacion)
    fechaCreacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    # auto_now > se modificara cada vez que se haga un update al registro en la base de datos almacena la hora y fecha actual
    fechaActualizacion = models.DateTimeField(auto_now=True, db_column='fecha_actualizacion')
    tipo = models.TextField(choices=tipoUsuario, default='CLIENTE')
    tipoDocumento = models.TextField(db_column='tipo_documento')
    numeroDocumento = models.TextField(db_column='numero_documento')
    telefono = PhoneNumberField(region='PE')

    # Columnas necesarias para trabajar con el panel administrativo
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # para realizar el login en el panel administrativo le indico cual sera la columna para identificar al usuario
    USERNAME_FIELD = 'correo'

    # Indicara los campos que de deben de pedir al momento de crear el super usuario por la terminal
    REQUIRED_FIELDS = ['nombre', 'apellido']

    class Meta:
        db_table = 'usuarios'

class CitaModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    dia = models.IntegerField(null=False)
    hora = models.TimeField(null=False)
    vehiculo = models.ForeignKey(to=VehiculoModel, on_delete=models.CASCADE, db_column='vehiculo_id')
    usuario = models.ForeignKey(to=UsuarioModel, on_delete=models.CASCADE, db_column='usuario_id')

    class Meta:
        db_table = 'citas'
        # sirve para crear una unicidad entre dos o mas columnas
        # un usuario no podra tener otra cita en el mismo dia y la misma hora
        # si tenemos mas de una unicidad grupal se creara un arreglo de arreglos, caso contrario no es necesario y puede trabajar todo en un solo arreglo
        unique_together = ['usuario','dia','hora']