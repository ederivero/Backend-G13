from flask_restful import Resource, request
from decorators import validador_usuario_admin

class SubirImagenController(Resource):

    @validador_usuario_admin
    def post(self):
        
        print(request.files)

        return {
            'message': 'Imagen subida exitosamente'
        }