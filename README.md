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

1. Sobre el directorio raíz ejecutar:
   - `docker-compose build`
   - `docker-compose up`

Esto levantará por primera vez los contenedores Docker, específicamente, levantará un contenedor con la base de datos y luego otro contenedor con el backend.

Se recomienda utilizar `docker-compose -d` para que sea detach, y luego `docker-compose down {id del contenedor a apagar}` para asegurar que se apaga el contenedor de manera correcta.

2. Luego de levantados los contenedores, ir a las rutas http://localhost:3006/ (ruta principal) y http://localhost:3006/api/ping. El resto de rutas están definidas en [routes](src/routes.py).

3. Para hacer reload del projecto podemos usar `docker-compose up -d --build --force-recreate`

# Dev

## BACKEND:

### Logica espacial

- [ ] En las clases, instructor y alumno no puede estar en 2 clases del mismo turno.
- [ ] En el horario de clases, estas no pueden ser modificadas o eliminadas.

### Create read update delete, Endpoints.

- [x] CRUD sobre Instructores.
- [ ] CRUD sobre Turnos.
- [ ] CRUD sobre Alumnos.
- [ ] RU sobre Actividades.
- [ ] RU sobre Clases, solo los campos, instructor, turno y agregar y quitar alumnos en las clases grupales. 
- [ ] Endpoint reportes.

---

## BASE DATOS

- [x] Inserciones de datos base.
- [ ] reportes

### Reportes:

- [ ] Actividades que más ingresos generan – se debe sumar el costo de equipamiento
- [ ] Actividades con más alumnos
- [ ] Los turnos más con más clases dictadas

---

# Endpoints

### . **Instructors (Instructores)**

- **Base URL:** `/api/Instructores`
- **Endpoints:**
  - `GET /api/Instructores`: Retrieve all instructors. x 
  - `GET /api/Instructores/<int:id>`: Retrieve a single instructor by CI. x 
  - `POST /api/Instructores`: Create a new instructor. x 
  - `PUT /api/Instructores/<int:id>`: Update an existing instructor by CI. x 
  - `DELETE /api/Instructores/<int:id>`: Delete an instructor by CI. x

### 2. **Schedules (Turnos)**

- **Base URL:** `/api/turnos`
- **Endpoints:**
  - `GET /api/turnos`: Retrieve all schedules.
  - `GET /api/turnos/<int:id>`: Retrieve a single schedule by ID.
  - `POST /api/turnos`: Create a new schedule. returns the id
  - `PUT /api/turnos/<int:id>`: Update an existing schedule by ID.
  - `DELETE /api/turnos/<int:id>`: Delete a schedule by ID.

### 3. **Activities (Actividades)**

- **Base URL:** `/api/actividades`
- **Endpoints:**
  - `GET /api/actividades`: Retrieve all activities.
  - `GET /api/actividades/<int:id>`: Retrieve a single activity by ID.
  - `PUT /api/actividades/<int:id>`: Update an existing activity by ID.

### 4. **Classes (Clases)**

- **Base URL:** `/api/clases`
- **Endpoints:**
  - `GET /api/clases`: Retrieve all classes.
  - `GET /api/clases/<int:id>`: Retrieve a single class by ID.
  - `PUT /api/clases/<int:id>`: Update fields for instructor, schedule, or modify enrolled students in group classes.

#### Student Management in Group Classes

- **Adding a alumnos to a class:** `POST /api/classes/<int:class_id>/alumnos/<int:alumnos_id>`
- **Removing a alumnos from a class:** `DELETE /api/classes/<int:class_id>/alumnos/<int:alumnos_id>`
- **Adding a instructor to a class:** `POST /api/classes/<int:class_id>/instructor/<int:instructor_id>`
- **Removing a instructor from a class:** `DELETE /api/classes/<int:class_id>/instructor/<int:instructor_id>`

### Reportes

- **base URL**: `/api/reportes`
  - **Actividad con más ingresos**: `/api/reportes/actividad_mas_ingresos`
  - **Actividad con más alumnos**: `/api/reportes/actividad_mas_alumnos`
  - **Turnos con mas clases dictadas**: `/api/reportes/turnos_mas_frecuentes`

---

## FRONTEND:

### Páginas y vistas principales

- [ ] Crear la página de **Estudiantes**:

  - Vista de lista de estudiantes.
  - Formulario de creación y edición de estudiantes.
  - Funcionalidad para eliminar estudiantes.

- [ ] Crear la página de **Clases**:

  - Vista de lista de clases.
  - Formulario de creación y edición de clases, que incluya selección de instructor y turno.
  - Funcionalidad para agregar y quitar estudiantes en clases grupales.

- [ ] Crear la página de **Instructores**:

  - Vista de lista de instructores.
  - Formulario de creación y edición de instructores.
  - Funcionalidad para eliminar instructores.

- [ ] Crear la página de **Turnos**:

  - Vista de lista de turnos.
  - Formulario de creación y edición de turnos.
  - Funcionalidad para eliminar turnos.

- [ ] Crear la página de **Actividades**:
  - Vista de lista de actividades.
  - Formulario de creación y edición de actividades.
  - Funcionalidad para eliminar actividades.

### Páginas de reportes

Sugerencia usar Tables de [mui](https://mui.com/material-ui/react-table/)

- [ ] Crear la página de **Reportes**:
  - Subvista de “Actividades que más ingresos generan” (con el costo de equipamiento sumado).
  - Subvista de “Actividades con más alumnos”.
  - Subvista de “Turnos con más clases dictadas”.
