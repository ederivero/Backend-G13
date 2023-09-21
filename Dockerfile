# primero indico que imagen utilizare para poder construir mi contenedor
FROM python:3.11.5-alpine

# indicar donde sera el directorio de trabajo 
WORKDIR /app

# crea la carpeta de trabajo dentro del contenedor
# esta ubicacion no existe en nuestra maquina, solo en el contenedor
# RUN mkdir -p /app

# copia todo el contenido local hacia la carpeta creada anteriormente
COPY . .

RUN apk update \
    && apk add musl-dev libpq-dev gcc

# ejecuta un comando pero a diferencia del CMD este comando no debe ser para levantar el contenedor
RUN pip install -r requirements.txt

# exponemos el puerto que podra acceder al contenedor de manera externa
EXPOSE 8000

# ejecutar el comando
CMD ["python", "notas/manage.py", "runserver"]