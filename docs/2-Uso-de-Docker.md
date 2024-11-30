# Uso de Docker

En el proyecto, Docker se utiliza para simplificar la gestión y despliegue de los servicios, garantizando un entorno consistente y fácil de replicar. Todo el sistema se levanta utilizando contenedores Docker independientes para los diferentes componentes de la aplicación.

---

## Arquitectura de Contenedores

El proyecto se compone de tres contenedores Docker separados:

Base de Datos:
- Proporciona almacenamiento y gestión de datos persistentes.
- Configurada para garantizar una comunicación fluida con el backend.
- Sus datos se persisten en un volumen aislado.

Backend:
- Implementa la lógica de negocio y la API que conecta el frontend con la base de datos.
- Se ejecuta de manera aislada en su propio contenedor.

Frontend:
- Maneja la interfaz de usuario y consume los datos proporcionados por el backend.
- Desplegado en un contenedor separado para mantener la modularidad.

`Nota:` Este [diagrama](./diagrams/ArquitecturaContenedoresDocker.png) muestra cómo se interconectan los contenedores.

## Configuración con Docker Compose

Para simplificar la configuración y el manejo de los contenedores, se utiliza un archivo [docker-compose.yml](../docker-compose.yml).

`Nota:` El archivo `docker-compose.yml` está comentado en todas sus líneas para aclarar detalles de configuración.

Este archivo define:

- Las imágenes Docker (plantillas de contenedores) necesarias para cada componente (ej. imagen mysql para el servicio de la base de datos).
- Las redes y volúmenes para facilitar la comunicación entre los servicios y la persistencia de datos (ej. db_data para persitir datos, ucu_network para conectar los servicios).
- Las variables de entorno requeridas para cada servicio (ej. el nombre de la base de datos que lo necesita el backend).

## Uso de Dockerfile

Cada componente del proyecto que no utiliza imágenes prediseñadas cuenta con su propio Dockerfile, donde se define cómo construir el contenedor desde cero.

- [Dockerfile del backend](../backend/Dockerfile): Se definen las dependencias a instalar, la imagen a utilizar, los comandos para ejecutar, etc.

- [Dockerfile del frontend](../frontend/Dockerfile): Define los mismos ítems que el Dockerfile de backend.

## Ejecución de Scripts MySQL en la Base de Datos

En el archivo [docker-compose.yml](../docker-compose.yml), se define la carpeta de scripts MySQL que se ejecutarán sobre la base de datos la primera vez que se levante en un contenedor.

Los [scripts MySQL](../scripts/) se encuentran ordenados en la carpeta de forma alfabética, lo cual le dice al contenedor el orden de ejecución de los archivos.

`Nota:` Estos scripts MySQL sólo se ejecutarán la primera vez que se levante el contenedor con la base de datos, por lo tanto, hacer un rebuild del proyecto no los volverá a ejecutar y, además, no borrará los datos guardados en la base de datos.

## Ventajas del Uso de Docker y Dockerfile

- Modularidad: Cada componente tiene su propio contenedor, lo que asegura independencia y facilidad de mantenimiento.
- Personalización: Los Dockerfile permiten definir entornos específicos según las necesidades del proyecto.
- Escalabilidad: Al usar contenedores separados, cada servicio puede escalarse de forma independiente según la demanda.
- Simplicidad: El archivo docker-compose.yml automatiza el despliegue, asegurando consistencia en diferentes entornos.