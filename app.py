from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from utilitarios import conexion
from flask_cors import CORS
from os import environ
from dotenv import load_dotenv
from models import *


# sirve para cargar mis variables declaradas en el archivo .env como si fueran variables de entorno
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=environ.get('DATABASE_URL')
# CORS > Cross Origin Resource Sharing (sirve para indicar quien puede tener acceso a mi API, indicando el dominio (origins), las cabeceras (allow_headers), y los metodos (methods))
CORS(app, origins='*')
api = Api(app)

conexion.init_app(app)

Migrate(app, conexion)



if __name__ == '__main__':
    app.run(debug=True)