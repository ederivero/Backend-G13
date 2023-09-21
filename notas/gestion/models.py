from django.db import models
# PermissionsMixin > modificar la forma en la cual se dan los permisos a los usuarios creados para el panel administrativo
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# reutilizaremos la tabla auth_user que nos crea django
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField(unique=True, null=False)
    nombre = models.TextField()
    apellido = models.TextField()
    fechaCreacion = models.DateField(
        auto_now_add=True, db_column='fecha_creacion')

    # si queremos seguir utilizando el panel administrastivo de django, tenemos que agregar las columnas is_staff, is_active para poder tener acceso
    # is_staff > valida que el usuario registrado pueda tener permisos para acceder al panel administrativo
    is_staff = models.BooleanField(default=False)

    # is_active > valida si el usuario esta activado para que puedan realizar operaciones ya sea superusuario o no
    is_active = models.BooleanField(default=True)

    # para que puedan hacer login en el panel administrativo tenemos que indicar que columna usaremos para identificar al usuario
    USERNAME_FIELD = 'correo'

    # cuando creemos un usuario por consola (python manage.py createsuperuser) tenemos que indicar que columnas tienen que ser requeridas
    REQUIRED_FIELDS = ['nombre']

    class Meta:
        db_table = 'usuarios'


class Nota(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.TextField(null=False)
    descripcion = models.TextField()
    tipo = models.TextField(choices=(('LISTA', 'LISTA'), ('TEXTO', 'TEXTO')))
    imagen = models.ImageField(upload_to='imagenes_notas/')
    fechaCreacion = models.DateTimeField(
        auto_now_add=True, db_column='fecha_creacion')
    fechaActualizacion = models.DateTimeField(
        auto_now=True, db_column='fecha_actualizacion')

    usuario = models.ForeignKey(
        to=Usuario, on_delete=models.PROTECT, db_column='usuario_id')

    class Meta:
        db_table = 'notas'


class Item(models.Model):
    titulo = models.TextField(null=False)
    completado = models.BooleanField(default=False)
    fechaCreacion = models.DateTimeField(
        auto_now_add=True, db_column='fecha_creacion')

    nota = models.ForeignKey(
        to=Nota, on_delete=models.PROTECT, db_column='nota_id')

    class Meta:
        db_table = 'items'
