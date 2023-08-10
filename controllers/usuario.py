from models import UsuarioModel
from utilitarios import conexion
from flask_restful import Resource, request
from dtos import UsuarioRequestDto, UsuarioResponseDto, LoginRequestDto
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token

class RegistroController(Resource):
    def post(self):
        """
        file: registroUsuarioSwagger.yml
        """
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
        

class LoginController(Resource):
    def post(self):
        """
        file: loginSwagger.yml
        """
        dto = LoginRequestDto()
        try:
            dataValidada = dto.load(request.get_json())
            # busco si el usuario existe
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(correo = dataValidada.get('correo')).first()

            if not usuarioEncontrado:
                return {
                    'message': 'El usuario no existe'
                }, 400

            password = bytes(usuarioEncontrado.password, 'utf-8')
            passwordEntrante = bytes(dataValidada.get('password'), 'utf-8')

            # validara si es la password o no
            resultado = checkpw(passwordEntrante, password)

            if resultado == False:
                return {
                    'message': 'Credenciales incorrectas'
                },400
            
            # identity > identificador para indicar a quien le pertenecera esta token
            token = create_access_token(identity= usuarioEncontrado.id)

            print(token)
            return {
                'content': token
            }

        except Exception as e:
            return {
                'message': 'Error al hacer el login',
                'content': e.args
            },400