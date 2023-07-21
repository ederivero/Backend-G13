-- Creamos un nuevo usuario para que pueda acceder a nuestro servidor
CREATE ROLE "ederi" WITH LOGIN SUPERUSER PASSWORD 'password';

CREATE DATABASE minimarket;

-- Mostrarnos la hora y fecha actual del servidor
SELECT NOW();
SELECT CURRENT_TIMESTAMP;
-- Mostrarnos la fecha actual
SELECT CURRENT_DATE;

-- Mostrarnos la hora actual del servidor
SELECT CURRENT_TIME;

-- Crear una tabla llamada categorias en la cual se tiene las sgtes columnas
-- id autoincrementable pk
-- nombre texto no puede ser nula y tiene que unica
-- estado que va a ser boolean y su valor por defecto va a ser true
-- color y este sera un texto que puede ser nula 
-- fecha_creacion que va a ser fecha y su valor por defecto sera now()
CREATE TABLE categorias(
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    estado BOOLEAN DEFAULT true,
    color TEXT NULL,
    fecha_creacion TIMESTAMP(3) DEFAULT NOW()
);

CREATE TABLE categorias(
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nombre TEXT NOT NULL UNIQUE,
    estado BOOLEAN DEFAULT true,
    color TEXT NULL,
    fecha_creacion TIMESTAMP(3) DEFAULT NOW()
);


-- Abarrotes true #ABABCD
-- Limpieza true #1E2C9F
-- Frutas false #15935B
INSERT INTO categorias (nombre, estado, color) VALUES
                       ('Abarrotes', true, '#ABABCD'),
                       ('Limpieza', true, '#1E2C9F'),
                       ('Frutas', false, '#15935B');



CREATE TABLE productos(
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nombre TEXT NOT NULL,
    precio FLOAT NOT NULL,
    foto TEXT,
    disponible BOOLEAN,
    categoria_id UUID NOT NULL,
    -- Asi se crean las relaciones
    -- primero ponemos un nombre a la relacion
    -- luego usamos una columna de la tabla local y creamos la referencia TABLA_FORANEA(columna)
    CONSTRAINT fk_categorias FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);


INSERT INTO productos (nombre, precio, foto, disponible, categoria_id) VALUES
                        -- Los 3 primeros son de abarrotes
                        ('Serrucho', 14.50, 'https://picsum.photos/200', true, '86bf8b7a-3611-4497-a68b-6d73c95faebd'),
                        ('Esponja de lavar', 4.80, 'https://picsum.photos/200', false, '86bf8b7a-3611-4497-a68b-6d73c95faebd'),
                        ('Paño de microfibra', 9.90, 'https://picsum.photos/200', true, '86bf8b7a-3611-4497-a68b-6d73c95faebd'),
                        -- Los 5 siguientes son de Limpieza
                        ('Detergente', 24.90, 'https://picsum.photos/200', true, 'b5789aa9-66e8-4f63-8a85-cf778bd864c7'),
                        ('Cepillo dental', 12.50, 'https://picsum.photos/200', false, 'b5789aa9-66e8-4f63-8a85-cf778bd864c7'),
                        ('Shampoo', 34.00, 'https://picsum.photos/200', true, 'b5789aa9-66e8-4f63-8a85-cf778bd864c7'),
                        ('Cloro', 5.20, 'https://picsum.photos/200', true, 'b5789aa9-66e8-4f63-8a85-cf778bd864c7'),
                        ('Mr. Musculo', 19.80, 'https://picsum.photos/200', false, 'b5789aa9-66e8-4f63-8a85-cf778bd864c7'),
                        -- Los 4 siguientes son de Frutas
                        ('Uva', 4.00, 'https://picsum.photos/200', true, 'd4c5600e-385e-41a7-96fa-875f9964c0be'),
                        ('Manzana', 2.90, 'https://picsum.photos/200', true, 'd4c5600e-385e-41a7-96fa-875f9964c0be'),
                        ('Membrillo', 1.50, 'https://picsum.photos/200', false, 'd4c5600e-385e-41a7-96fa-875f9964c0be'),
                        ('Kion', 1.50, 'https://picsum.photos/200', true, 'd4c5600e-385e-41a7-96fa-875f9964c0be');