from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from utilitarios import conexion
from flask_cors import CORS
from os import environ
from dotenv import load_dotenv
from models import *
from flasgger import Swagger
from controllers import CategoriasController, RegistroController, LoginController
# convierte un string en formato json a un diccionario
from json import load


# sirve para cargar mis variables declaradas en el archivo .env como si fueran variables de entorno
load_dotenv()
swaggerData = load(open('swagger_data.json', 'r'))

# https://github.com/flasgger/flasgger#customize-default-configurations
swaggerConfig = {
    'headers': [], # las cabeceras que van a aceptar nuestra documentacion
    'specs': [
        {
            'endpoint': '', # el endpoint inicial de nuestra documentacion 
            'route': '/'
        }
    ],
    'static_url_path': '/flasgger_static', # cargar los archivos staticos que serian el css y js de la libreria
    # 'swagger_ui': True, # indicar si queremos cargar la interfaz grafica o no
    'specs_route' : '/documentacion' # el endpoint en el cual ahora se ingresara a mi swagger
}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=environ.get('DATABASE_URL')

Swagger(app, template=swaggerData, config=swaggerConfig)
# CORS > Cross Origin Resource Sharing (sirve para indicar quien puede tener acceso a mi API, indicando el dominio (origins), las cabeceras (allow_headers), y los metodos (methods))
CORS(app, origins='*')
api = Api(app)

conexion.init_app(app)

Migrate(app, conexion)

# rutas
api.add_resource(CategoriasController, '/categorias')
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')

if __name__ == '__main__':
    app.run(debug=True)