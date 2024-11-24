# Endpoints

- URI BASE: `http://localhost:3006/api`

### 0. De comprobación

- `/`: Muestra un mensaje de bienvenida.
- `/ping`: Comprueba si la conexión con la base de datos se puede establecer.

### 1. **Instructors (Instructores)** [x]

- **Base URI:** `/instructores`
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

- **Endpoints:**
  - `GET /equipamientos`: Retorna todos los equipamientos. [x]
  - `GET /equipamientos/<int:id>`: Retorna un único equipamiento por ID. [x]

### Reportes [ ]

- **Base URI**: `/reportes`
- **Endpoints:**
  - **Actividad con más ingresos**: `/reportes/actividad_mas_ingresos`
  - **Actividad con más alumnos**: `/reportes/actividad_mas_alumnos`
  - **Turnos con mas clases dictadas**: `/reportes/turnos_mas_frecuentes`