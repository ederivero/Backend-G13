from flask import Flask, request
from datetime import datetime
from psycopg2 import connect

conexion = connect(database="minimarket", user="postgres", password ="password", host="localhost", port="5432")
# __name__ > indicara si el archivo en el cual estamos es el archivo principal o no (__main__)
# en flask solamente se puede crear una instancia de la clase por proyecto para evitar tener varios servidores en mismo proyecto 

app = Flask(__name__)

# indicando que la ruta '/' aceptara GET y POST
@app.route('/', methods = ['GET', 'POST'])
def inicio():
    # request> se guadara toda la informacion que me envia el cliente (FE)
    # https://flask.palletsprojects.com/en/2.3.x/quickstart/#accessing-request-data

    print(request.method)
    if request.method == 'GET':
        return {
            'message': 'Bienvenido a mi API'
        }
    elif request.method == 'POST':
        return {
            'message': 'La hora del servidor es : %s'% (datetime.now())
        }

@app.route('/categorias', methods = ['GET', 'POST'])
def manejoCategorias():
    if request.method == 'GET':
        # creamos el cursor para poder interactuar con nuestra bd
        cursor = conexion.cursor()

        # indicamos la query a realizarse en la base de datos
        cursor.execute("SELECT * FROM categorias;")

        # devolvera todos los resultados
        data = cursor.fetchall()

        # cerramos el uso de nuestra bd
        cursor.close()

        resultado = []
        
        for categoria in data:
            dataCategoria = {
                'id': categoria[0],
                'nombre': categoria[1],
                'estado': categoria[2],
                'color': categoria[3],
                'fechaCreacion': categoria[4]
            }
            resultado.append(dataCategoria)
            print(dataCategoria)

        return {
            'content': resultado
        }
    
    elif request.method == 'POST':
        print(request.json)

        return {
            'message': 'Categoria creada exitosamente'
        }


if __name__ == '__main__':
    # si es el archivo principal levantaremos nuestro proyecto
    app.run(debug=True)