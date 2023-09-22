from django.db import models
# PermissionsMixin > modificar la forma en la cual se dan los permisos a los usuarios creados para el panel administrativo
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# BaseUserManager > manejar o gestionar el comportamiento de los usuarios, esta clase se tiene que utilizar siempre y cuando hayamos modificado el diseño original del auth_user model
class ManejadorUsuario(BaseUserManager):
    def create_superuser(self, correo, nombre, password):
        # se utilizara para cuando querramos crear un superusuario por la terminal
        if not correo:
            raise ValueError('El usuario debe tener un correo')
        # remueve caracteres incorrectos y lo lleva el correo todo a minusculas para evitar duplicados
        correo_normalizado = self.normalize_email(correo)

        # el modelo modificado
        admin = self.model(correo=correo_normalizado, nombre=nombre)
        # ahora generamos el hash de la password
        admin.set_password(password)

        # seteamos los parametros del administrador
        admin.is_superuser = True
        admin.is_staff = True

        # guardamos el administrador en la base de datos
        admin.save()


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

    # le indicamos la funcionabilidad del metodo create_superuser en nuestro modelo usuario
    objects = ManejadorUsuario()

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
