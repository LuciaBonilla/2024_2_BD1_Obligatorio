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


# Dev
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
--- 
## BACKEND:
### Logica espacial
- [ ] En las clases instructor y alumno no puede estar en 2 clases del mismo turno.
- [ ] En el horario de clases estas no pueden ser modificadas o eliminadas.
### Create read update delete, Endpoints.
- [ ] CRUD sobre Instructores.
- [ ] CRUD sobre Turnos.
- [ ] CRUD sobre Actividades.
- [ ] RU sobre Actividades.
- [ ] RU sobre Clases, solo los campos, instructor, turno y agregar y quitar alumnos en las clases grupales.
- [ ] Endpoint reportes
---
## BASE DATOS
- [ ] Inserciones de datos base. 
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
    - `GET /api/Instructores`: Retrieve all instructors.
    - `GET /api/Instructores/<int:id>`: Retrieve a single instructor by CI.
    - `POST /api/Instructores: Create a new instructor.
    - `PUT /api/Instructores/<int:id>`: Update an existing instructor by CI.
    - `DELETE /api/Instructores/<int:id>`: Delete an instructor by CI.

### 2. **Schedules (Turnos)**

- **Base URL:** `/api/turnos`
- **Endpoints:**
    - `GET /api/turnos: Retrieve all schedules.
    - `GET /api/turnos/<int:id>`: Retrieve a single schedule by ID.
    - `POST /api/turnos`: Create a new schedule. returns the id 
    - `PUT /api/turnos/<int:id>`: Update an existing schedule by ID.
    - `DELETE /api/turnos/<int:id>`: Delete a schedule by ID.

### 3. **Activities (Actividades)**

- **Base URL:** `/api/actividades`
- **Endpoints:**
    - `GET /api/actividades`: Retrieve all activities.
    - `GET /api/actividades/<int:id>`: Retrieve a single activity by ID.
    - `POST /api/actividades`: Create a new activity.
    - `PUT /api/actividades/<int:id>`: Update an existing activity by ID.
    - `DELETE /api/actividades/<int:id>`: Delete an activity by ID.

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
	- **Actividad con más ingresos**:  `/api/reportes/actividad_mas_ingresos`
	- **Actividad con más alumnos**:  `/api/reportes/actividad_mas_alumnos`
	- **Turnos con mas clases dictadas**:  `/api/reportes/turnos_mas_frecuentes`
