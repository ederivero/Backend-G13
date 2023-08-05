from models import UsuarioModel
from utilitarios import conexion
from flask_restful import Resource, request
from dtos import UsuarioRequestDto, UsuarioResponseDto
from bcrypt import gensalt, hashpw

class RegistroController(Resource):
    def post(self):
        try:
            dto =UsuarioRequestDto()
            dataValidada = dto.load(request.get_json())
            # generar el hash de las password
            # creara un texto aleatorio
            salt = gensalt()

            password = dataValidada.get('password')

            # convertimos el password a bytes
            passwordBytes = bytes(password,'utf-8')

            # mezclamos el password con el salt generado y lo convertimos a string
            passwordHasheada = hashpw(passwordBytes, salt).decode('utf-8')

            # sobreescribimos la pasword con el hash generado
            dataValidada['password'] = passwordHasheada

            # fin del hashing de la password

            nuevoUsuario = UsuarioModel(**dataValidada)

            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            dtoResponse = UsuarioResponseDto()

            return {
                'message': 'Usuario creado exitosamente',
                'content': dtoResponse.dump(nuevoUsuario)
            }, 201
        except Exception as e:
            return {
                'message': 'Error al crear el usuario',
                'content': e.args
            },400