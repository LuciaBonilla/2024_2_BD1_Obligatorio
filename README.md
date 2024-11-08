# 2024_2_BD1_Obligatorio

## Estructura de carpetas

- En [src](src) está la aplicación de backend (aplicación Flask) y los archivos necesarios (Dockerfile y requirements.txt) para levantar la aplicación en un contenedor Docker.

- En [docs](docs) están los diagramas de tablas de la base de datos.

- En [scripts](scripts) están los scripts MySQL para crear tablas, insertar datos maestro y controlar permisos.

## Pasos para probar el backend y la base de datos

1) Sobre el directorio raíz ejecutar
    - `docker-compose build`
    - `docker-compose up` 

Se recomeinda utilizar `docker-compose -d` para que sea detach, y luego `docker-compose down` para asegurarte que se cierra la base de datos de manera correcta 

Esto levantará el contenedor Docker con la base de datos y luego el contenedor con el backend.

2) Luego de levantados los contenedores, ir a las rutas http://localhost:3006 y http://localhost:3006/db-check

3) Para hacer reload del projecto podemos usar `docker-compose up -d --build --force-recreate`
