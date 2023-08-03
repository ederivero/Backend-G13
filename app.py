from flask import Flask
from base_de_datos import conexion
from models.mascota import MascotaModel
# convierte caracteres especiales a un formato 'seguro'
from urllib.parse import quote_plus
from flask_migrate import Migrate
from flask_restful import Api
from controllers.usuario import UsuariosController, UsuarioController
from controllers.mascota import MascotasController
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from os import environ
from dotenv import load_dotenv

# load_dotenv tiene que estar en la primera linea de nuestro archivo principal
# cargara las variables del archivo .env y podran ser utilizadas en todo el proyecto
load_dotenv()

app = Flask(__name__)
api = Api(app)
# origins > indica los dominios que pueden acceder a mi API (*)
# methods > indica los metodos a los que se puede acceder (*)
# allow_headers > indica las cabeceras que podra recibir mi API (*)
CORS(app, origins=['https://editor.swagger.io', 'http://mifrontend.com'], 
     methods=['GET', 'POST', 'PUT', 'DELETE'],
                    # authorization > para cuestiones de autorizacion 
                    # content-type > ver la informacion que nos esta enviando el cliente
                    # accept > ver que es lo que aceptara el cliente | 
     allow_headers= ['authorization', 'content-type','accept'])

# endpoint donde se podra acceder a la documentacion
SWAGGER_URL = '/docs'
# donde se almacena mi archivo de la documentacion
API_URL='/static/documentacion_swagger.json'

configuracionSwagger = get_swaggerui_blueprint(SWAGGER_URL, API_URL,config={
    # el nombre de la pestaña del navegador
    'app_name':'Documentacion de Directorio de Mascotas' 
})

# agregar otra aplicacion que no sea Flask a nuestro proyecto de Flask
app.register_blueprint(configuracionSwagger)

# config > se van a guardar todas la variables de nuestro proyecto de flask
# CONNECTION STRING>                     dialecto://usuario   :password@  host   :port/ database
# postgres | mysql | mariadb | sqlite | sqlserver | oracle
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/directorio' % quote_plus('password')

# inicializar mi aplicacion de flask sql alchemy 
# dentro de la aplicacion de flask tendremos nuestra conexion a la base de datos
conexion.init_app(app)


# https://flask-migrate.readthedocs.io/en/latest/index.html#alembic-configuration-options
# app > sirve para que migrate use la cadena de conexion dentro del config
# db > sirve para indicar la conexion que ya esta realizada por nuestra configuracion previa
Migrate(app=app, db=conexion)

# @app.route('/crear-tablas',methods=['GET'])
# def crearTablas():
#     # creara todas las tablas declaradas en el proyecto
#     conexion.create_all()
#     return {
#         'message': 'Creacion ejecutada exitosamente'
#     }

# Aca agregamos todoas las rutas de nuestros controladores
api.add_resource(UsuariosController, '/usuarios')
api.add_resource(UsuarioController, '/usuario/<int:id>')
api.add_resource(MascotasController, '/mascotas')

if __name__ == '__main__':
    app.run(debug=True)