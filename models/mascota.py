from sqlalchemy import Column, types
from base_de_datos import conexion
from enum import Enum

class TipoMascota(Enum):
    Perro = 'Perro'
    Gato = 'Gato'
    Cuy = 'Cuy'

class SexoMascota(Enum):
    Macho = 'Macho'
    Hembra = 'Hembra'
    Helicoptero = 'Helicoptero'
    Otro = 'Otro'

class MascotaModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    tipo = Column(type_=types.Enum(TipoMascota), nullable=False)
    sexo = Column(type_=types.Enum(SexoMascota), default=SexoMascota.Otro)
    fechaNacimiento = Column(type_=types.Date, name='fecha_nacimiento')
    # Relaciones
    

    __tablename__ = 'mascotas'