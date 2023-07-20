-- Hacer uso del SELECT

SELECT nombre, correo FROM alumnos;

SELECT * FROM alumnos;

-- Para agregar filtros usamos la clausula WHERE
-- where > donde
SELECT * FROM alumnos WHERE matriculado = true;

-- El texto SIEMPRE en comillas simples, no usar comillas dobles ya que estas se usan para definir nombres de tablas con caracteres especiales o bases de datos
SELECT * FROM alumnos WHERE matriculado = true AND nombre = 'Juanito';


-- 1. Listar los nombres y fecha_nacmiento de los alumnos que sean Maria , Roberto O Maximo
SELECT nombre, fecha_nacimiento FROM alumnos WHERE nombre = 'Maria' OR nombre = 'Roberto' OR nombre='Maximo';
-- IN > colocamos todos los posibles valores en un arreglo 
SELECT nombre, fecha_nacimiento FROM alumnos WHERE nombre IN ('Maria', 'Roberto', 'Maximo');


-- 2. Devolver todos los alumnos que esten matriculados y que su nombre sea juanito o su apellido sea Tari Ramos
SELECT * FROM alumnos WHERE matriculado = true AND (nombre ='Juanito' OR apellidos='Tari Ramos');

