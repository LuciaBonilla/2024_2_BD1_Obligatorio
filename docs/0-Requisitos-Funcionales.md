# Introducción

El próximo semestre, la UCU planea abrir una escuela de deportes de nieve cómo una forma de ampliar la propuesta de deportes y de actividades ofreciendo una experiencia única.

En un comienzo, la escuela contara con 3 actividades: snowboard, ski y moto de nieve. Estas actividades tienen un costo asociado y una restricción de edad. 

La escuela tiene varios instructores ―no especializados, es decir, pueden dar clase de cualquier actividad― los cuales ofrecen los siguientes turnos para las clases: 
- De 9:00 a 11:00 
- De 12:00 a 14:00 
- De 16:00 a 18:00

Estas clases pueden ser grupales o individuales.

De los alumnos interesa guardar la siguiente información: 
- CI 
- Nombre 
- Apellido 
- Fecha de nacimiento 
- Teléfono de contacto 
- Correo electrónico

Como no todos los alumnos poseen equipamiento propio, ya que se trata de deportes poco comunes en Uruguay, la escuela ofrece alquiler de equipo ―desde antiparras, cascos, tablas de snowboard, esquíes, etc. Es necesario registrar si un alumno alquila o utiliza su equipamiento propio, ya que si se alquila el costo de la clase es mayor.

La UCU está buscando implementar un primer acercamiento a un sistema administrativo, que facilite a los administrativos de la escuela:

- Alta, baja y modificación (ABM) de instructores 
- ABM de turnos 
- Modificación de las actividades 
- ABM de alumnos 

Con respecto a las clases, en el día de la fecha, es importante tener en cuenta que un instructor no puede dar 2 clases en el mismo turno y que un alumno no puede estar inscripto en 2 clases distintas en el mismo turno. Además, las clases no pueden ser modificadas ni eliminadas durante el horario de esta, únicamente se pueden alterar antes o después de la misma. Los datos que se  pueden modificar son: 

- Instructor que da la clase 
- Turno 
- Agregar y quitar alumnos de las clases grupales

Con el fin de evaluar el éxito de la escuela, se solicita además un sistema de reportes donde se pueda consultar: 

- Actividades que más ingresos generan – se debe sumar el costo de equipamiento 
- Actividades con más alumnos 
- Los turnos más con más clases dictadas

# Requisitos Funcionales

---

## Dockerización

- [x] Bases de Datos.
- [x] Backend.
- [x] Frontend.

---

## Seguridad

- [x] Evitar inyección SQL.

---

## Backend

### Lógica espacial

- [ ] En las clases, instructor y alumno no puede estar en 2 clases del mismo turno.
- [ ] En el horario de clase, esta no puede ser modificada o eliminada.

### Create Read Update Delete (Endpoints)

- [x] CRUD sobre Instructores.
- [ ] CRUD sobre Turnos.
- [ ] CRUD sobre Alumnos.
- [ ] RU sobre Actividades.
- [ ] RU sobre Clases, solo los campos: instructor, turno, y agregar y quitar alumnos en las clases grupales.
- [ ] R reportes.

### Reportes

- [ ] Actividades que más ingresos generan – se debe sumar el costo de equipamiento.
- [ ] Actividades con más alumnos.
- [ ] Los turnos más con más clases dictadas.

---

## Base de Datos

- [x] Creación de tablas.
- [x] Inserción de datos base.

---

## Frontend

### Páginas y Vistas Principales

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