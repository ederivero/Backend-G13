from base_de_datos import conexion
from models.mascota import MascotaModel
from flask_restful import Resource, request
from dtos.mascota import MascotaRequestDto

class MascotasController(Resource):
    def post(self):
        body = request.get_json()
        dto = MascotaRequestDto()
        try:
            dataValidada = dto.load(body)
            nuevaMascota = MascotaModel(**dataValidada)
            conexion.session.add(nuevaMascota)
            conexion.session.commit()
            
            return {
                'message': 'Mascota creada exitosamente'
            }, 201
        
        except Exception as e:
            return {
                'message': 'Error al crear la mascota',
                'content': e.args
            }, 400
