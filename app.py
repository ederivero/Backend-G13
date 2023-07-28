from flask import Flask
from base_de_datos import conexion
from models.mascota import MascotaModel
# convierte caracteres especiales a un formato 'seguro'
from urllib.parse import quote_plus
from flask_migrate import Migrate
from flask_restful import Api
from controllers.usuario import UsuariosController


app = Flask(__name__)
api = Api(app)

# config > se van a guardar todas la variables de nuestro proyecto de flask
# CONNECTION STRING>                     dialecto://usuario   :password@  host   :port/ database
# postgres | mysql | mariadb | sqlite | sqlserver | oracle
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/directorio' % quote_plus('password')

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

if __name__ == '__main__':
    app.run(debug=True)