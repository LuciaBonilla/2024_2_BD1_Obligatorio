# Endpoints

### . **Instructors (Instructores)**

- **Base URL:** `/api/Instructores`
- **Endpoints:**
  - `GET /api/Instructores`: Retrieve all instructors. [x]
  - `GET /api/Instructores/<int:id>`: Retrieve a single instructor by CI. [x]
  - `POST /api/Instructores`: Create a new instructor. [x]
  - `PUT /api/Instructores/<int:id>`: Update an existing instructor by CI. [x]
  - `DELETE /api/Instructores/<int:id>`: Delete an instructor by CI. [x]

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