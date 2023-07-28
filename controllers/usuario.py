from base_de_datos import conexion
from models.usuario import UsuarioModel
from flask_restful import Resource, request

class UsuariosController(Resource):
    # cuando creamos un metodo con el mismo nombre que el metodo http si se llama a este metodo se ingresara al metodo de la clase
    def get(self):
        return {
            'message': 'Hola desde usuarios controller'
        }

    def post(self):
        data:dict = request.get_json()
        print(data)
        # { 'nombre' : 'Eduardo', 'apellido': 'de Rivero' ,...}
        nuevoUsuario = UsuarioModel(nombre = data.get('nombre',''), 
                     apellido = data.get('apellido',''), 
                     correo=data.get('correo'),
                     telefono = data.get('telefono'),
                     linkedinUrl = data.get('linkedinUrl'))
        # agregamos el nuevo registro a la cola del cursor    
        conexion.session.add(nuevoUsuario)
        # guardamos de manera permanente nuestro usuario en la bd, si hay un error de validacion aca se emitira
        conexion.session.commit()
        return {
            'message': 'Hola desde usuarios asdasdasd'
        }
    