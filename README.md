# 2024_2_BD1_Obligatorio

## Patrón de arquitectura de software (MVC - Modelo–Vista–Controlador - Model-Controller-View)

El backend se basa en este patrón.

Su objetivo es separar las preocupaciones en tres componentes distintos, lo que facilita el mantenimiento, escalabilidad y reutilización del código. Los componente son:

1. Modelo (Model)
El Modelo representa la lógica de negocio de la aplicación. Es el responsable de gestionar los datos, las reglas de negocio, y la interacción con la base de datos.

Responsabilidad: Mantener y manejar los datos de la aplicación.

Acciones: Realiza operaciones como crear, leer, actualizar y eliminar datos (conocido como CRUD -> Create-Read-Update-Delete).

2. Vista (View)
La Vista es responsable de la presentación de los datos. Es la interfaz que interactúa con el usuario y muestra la información proveniente del modelo. La vista no contiene lógica de negocio ni de manipulación de datos, solo se encarga de presentar la información.

Responsabilidad: Mostrar los datos y manejar la interfaz de usuario.

Acciones: Recibe datos del modelo a través del controlador y los presenta al usuario de manera adecuada. Puede ser una página web, una ventana gráfica en una aplicación de escritorio, etc.

3. Controlador (Controller)
El Controlador actúa como intermediario entre el modelo y la vista. Recibe las entradas del usuario a través de la vista, procesa esa información (interactúa con el modelo) y actualiza la vista con los resultados. En esencia, el controlador maneja la lógica de flujo de la aplicación.

Responsabilidad: Procesar la entrada del usuario, interactuar con el modelo para obtener o modificar los datos y actualizar la vista.

Acciones: Controla la lógica de la aplicación, maneja las solicitudes del usuario y decide qué vista mostrar y qué datos cargar.

## Estructura de carpetas

- En el directorio principal están los archivos necesarios (docker-compose.yml y Dockerfile) para levantar la base de datos y la aplicación en contenedores Docker.

- En [src](src) está la aplicación de backend ([app](src/app.py); aplicación Flask), junto a:

    - Las definición de rutas [routes](src/routes.py).
    - El modelo [model](src/model/).
    - Los controladores [controllers](src/controllers/).
    - Los módulos a instalar para que funcione la aplicación [requirements](src/requirements.txt).

- En [docs](docs) están los diagramas de tablas de la base de datos, de arquitectura y de clases.

- En [scripts](scripts) están los scripts MySQL para crear tablas e insertar datos maestro. Estos scripts se ejecutarán al levantar los contenedores Docker por primera vez.

## Pasos para probar el backend y la base de datos

1) Sobre el directorio raíz ejecutar:
    - `docker-compose build`
    - `docker-compose up` 

Esto levantará por primera vez los contenedores Docker, específicamente, levantará un contenedor con la base de datos y luego otro contenedor con el backend.

Se recomienda utilizar `docker-compose -d` para que sea detach, y luego `docker-compose down {id del contenedor a apagar}` para asegurar que se apaga el contenedor de manera correcta. 

2) Luego de levantados los contenedores, ir a las rutas http://localhost:3006/ (ruta principal) y http://localhost:3006/api/ping. El resto de rutas están definidas en [routes](src/routes.py).

3) Para hacer reload del projecto se puede usar `docker-compose up -d --build --force-recreate`