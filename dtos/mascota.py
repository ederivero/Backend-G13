from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.mascota import MascotaModel

class MascotaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = MascotaModel
        # validara tbn las columnas que son llaves foraneas
        include_fk = True