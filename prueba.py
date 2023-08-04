from psycopg2 import connect

conector = connect(database='postgres', 
        user='postgres', 
        password='password', 
        host='localhost',
        port='5432')
conector.autocommit = True

cursor = conector.cursor()

def crearBD(bd):
    cursor.execute('SELECT datname FROM pg_database')
    resultado = cursor.fetchall()
    # [('xxxx',), ('yyyy',), ('bd',)]
    if (bd,) in resultado:
        print('ya existe!')
        return

    cursor.execute(f'CREATE DATABASE {bd}')
    # cursor.execute('CREATE DATABASE {}'.format(bd))

    print('BASE DE DATOS CREADA EXITOSAMENTE')
    conector.close()


crearBD('prueba3')