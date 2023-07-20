-- SQL > Structured Query Language

-- DDL (Data Definition Language)
-- CREATE > Crear tablas o bases de datos 
-- ALTER  > Modificar la estructura de nuestras tablas o columnas
-- DROP   > Eliminar tablas, columnas o bases de datos
-- TRUNCATE > Eliminar todos los registros de una tabla
-- COMMENT > Agregar comentarios
-- RENAME > Renombrar tablas, columnas, bases de datos

CREATE DATABASE prueba;

-- NOTA: para los comandos PSQL porque empiezan con \ no es necesario colocar el ';' al final
\c prueba -- > sirve para cambiarnos a la base de datos escrita, si no existe lanzara un error


CREATE TABLE alumnos (
id SERIAL NOT NULL PRIMARY KEY,
nombre TEXT NOT NULL,
apellidos TEXT,
correo TEXT NOT NULL UNIQUE, -- UNIQUE > significa que el valor no se puede repetir en otro registro
fecha_nacimiento DATE NOT NULL,
matriculado BOOLEAN DEFAULT true -- DEFAULT > sirve para setear un valor por defecto en el caso no se ingrese
);

