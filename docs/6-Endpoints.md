# Endpoints

### Aclaraciones

1. URI Base:

Todas las rutas tienen como base: `http://localhost:3006/api`

2. Postman:

Se recomienda usar Postman, una herramienta útil para probar APIs en desarrollo web y aplicaciones móviles.

3. Colección Postman:

Se utilizó esta [colección de Postman](./Obligatorio.postman_collection.json) para probar los endpoints de la API.

4. Autenticación:

Todos los endpoints requieren enviar un JSON que incluya las credenciales de administrador por defecto:

`
{
    "login": {
        "correo": "admin@mail.com",
        "contrasena": "123"
    }
}
`

Estas credenciales corresponden a una cuenta de administrador creada automáticamente en la tabla `LOGIN` de la base de datos ([ver script de insert en la base de datos](../scripts/2_insert-master-data.sql)).
Esto añade una capa básica de seguridad para interactuar con la base de datos, ya que el backend no procesará ninguna operación si el registro asociado al login enviado no se encuntra en la base.

5. Advertencia sobre Prácticas de Seguridad:

Enviar credenciales en el cuerpo de una solicitud HTTP no es la práctica más segura, ya que:

- Las contraseñas pueden almacenarse en logs o ser interceptadas si no se usa HTTPS.
- Es preferible implementar un sistema donde las credenciales solo se envían una vez para obtener un token cifrado, como JWT, el cual se usa en solicitudes posteriores.

Sin embargo, utilizar esta práctica no tan segura ha permitido agregar fácilmente un poco de seguridad.

### 0. **De comprobación**

- `/`: Muestra un mensaje de bienvenida. [x]
- `/ping`: Comprueba si la conexión con la base de datos se puede establecer. [x]

### 1. **Instructors (Instructores)** [x]

- **Base URI:** `/instructores` [x]
- **Endpoints:**
  - `GET /instructores`: Retorna todos los instructores. [x]
  - `GET /instructores/<int:ci>`: Retorna un único instructor por CI. [x]
  - `POST /instructores`: Crea un nuevo instructor. Retorna CI. [x]
  - `PATCH /instructores/<int:ci>`: Actualiza un instructor por CI. Retorna CI. [x]
  - `DELETE /instructores/<int:ci>`: Elimina un instructor por CI. [x]

### 2. **Schedules (Turnos)** [x]

- **Base URI:** `/turnos`
- **Endpoints:**
  - `GET /turnos`: Retorna todos los turnos. [x]
  - `GET /turnos/<int:id>`: Retorna un único turno por ID. [x]
  - `POST /turnos`: Crea un nuevo turno. [x]
  - `PATCH /turnos/<int:id>`: Actualiza un turno por ID. Retorna ID. [x]
  - `DELETE /turnos/<int:id>`: Elimina un turno por ID. [x]

### 3. **Activities (Actividades)** [x]

- **Base URI:** `/actividades`
- **Endpoints:**
  - `GET /actividades`: Retorna todas las actividades. [x]
  - `GET /actividades/<int:id>`: Retorna una única actividad por ID. [x]
  - `PATCH /actividades/<int:id>`: Actualiza una actividad por ID. Retorna ID. [x]

### 4. **Students (Alumnos)** [x]

- **Base URI:** `/alumnos`
- **Endpoints:**
  - `GET /alumnos`: Retorna todos los alumnos. [x]
  - `GET /alumnos/<int:ci>`: Retorna un único alumno por CI. [x]
  - `POST /alumnos`: Crea un nuevo alumno. Retorna CI. [x]
  - `PATCH /alumnos/<int:ci>`: Actualiza un alumno por CI. Retorna CI. [x]
  - `DELETE /alumnos/<int:ci>`: Elimina un alumno por CI. [x]

### 5. **Classes (Clases)** [x]

- **Base URI:** `/clases`
- **Endpoints:**
  - `GET /clases`: Retorna todas los clases. [x]
  - `GET /clases/<int:ci>`: Retorna una única clase por ID. [x]
  - `POST /clases`: Crea un nueva clase. [x]
  - `PATCH /clases/<int:ci>`: Actualiza una clase por ID. Retorna ID. [x]
  - `DELETE /clases/<int:ci>`: Elimina una clase por ID. [x]

### 6. **Assistances (Asistencias)** [x]

- **Base URI:** `/asistencias`
- **Endpoints:**
  - `GET /asistencias`: Retorna todas las asistencias. [x]
  - `GET /asistencias/clases/<int:id>/alumnos/<int:ci>`: Retorna una única asistencia por ID de la clase y CI del alumno. [x]
  - `POST /asistencias`: Crea un nueva asistencia. Retorna ID de la clase, CI del alumno e ID del equipamiento. [x]
  - `PATCH /asistencias/clases/<int:id>/alumnos/<int:ci>`: Actualiza una asistencia por ID de la clase y CI del alumno. Retorna ID de la clase, CI del alumno e ID del equipamiento. [x]
  - `DELETE /asistencias/clases/<int:id>/alumnos/<int:ci>`: Elimina una clase por ID de la clase y CI del alumno. [x]

### 7. **Equipments (Equipamientos)** [x]

- **Base URI**: `/equipamientos`
- **Endpoints:**
  - `GET /equipamientos`: Retorna todos los equipamientos. [x]
  - `GET /equipamientos/<int:id>`: Retorna un único equipamiento por ID. [x]

### 8. **Reportes** [x]

- **Base URI**: `/reportes`
- **Endpoints:**
  - **Actividades con más ingresos**: `/reportes/actividades_mas_ingresos`
  - **Actividades con más alumnos**: `/reportes/actividades_mas_alumnos`
  - **Turnos con mas clases dictadas**: `/reportes/turnos_mas_frecuentes`