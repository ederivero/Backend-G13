-- DML  (Data Manipulation Language)

-- INSERT > Insertar valores a nuestras tablas
-- SELECT > Seleccionar data de nuestras tablas
-- UPDATE > Actualizar los registros de nuestras tablas
-- DELETE > Eliminar los registros de nuestras tablas

-- https://es.wikipedia.org/wiki/ISO_8601

INSERT INTO alumnos (id, nombre, apellidos, correo, fecha_nacimiento, matriculado) VALUES
                    (DEFAULT, 'Juanito', 'Perez Martinez', 'jperes@gmail.com', '2005-04-13', DEFAULT);


INSERT INTO alumnos (id, nombre, apellidos, correo, fecha_nacimiento, matriculado) VALUES
                    (DEFAULT, 'Maria', 'Salcedo Zegarra', 'msalcedo@hotmail.com', '2006-03-01', false),
                    (DEFAULT, 'Rosa', 'Berlanga Jhonson', 'rberlanga@gmail.com', '2005-12-13', false),
                    (DEFAULT, 'Roberto', 'Chuquihuaman Rojas', 'rchuquihuaman@outlook.com', '2004-07-21', true),
                    (DEFAULT, 'Maximo', 'Tari Ramos', 'mtari@gmail.com', '2005-10-09', false);
                    
