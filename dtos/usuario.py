from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuario import UsuarioModel

class UsuarioRequestDTO(SQLAlchemyAutoSchema):
    class Meta:
        # Meta > sirve para pasarle o definir los atributos a la clase que estoy heredando
        # al definir que modelo vamos a utilizar ya mapeara todos los atributos (columnas) necesarias y opcionales de la tabla
        model = UsuarioModel
        # pasarle metadata al padre o clase de la cual estoy heredando