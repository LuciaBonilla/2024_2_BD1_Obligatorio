-- Para aceptar letras con acentos.
ALTER DATABASE ucu_snow_sports DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;

/*
RANGOS NUMÉRICOS USADOS
TINYINT UNSIGNED: 0-255
MEDIUMINT UNSIGNED: 0-16777215
INTEGER UNSIGNED: 0-4294967295

FORMATO DE TIME: HH:MM:SS
FORMATO DE DATE: YYYY-MM-DD
*/

-- CREACIÓN DE LAS 8 TABLAS.
CREATE TABLE TURNOS (
    id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, -- PK
    
	hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL
);

CREATE TABLE ACTIVIDADES (
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, -- PK
    
    nombre VARCHAR(30) UNIQUE NOT NULL,
    descripcion VARCHAR(100),
    costo MEDIUMINT UNSIGNED NOT NULL,
    edad_minima TINYINT UNSIGNED NOT NULL
);

CREATE TABLE ALUMNOS (
	ci INTEGER UNSIGNED NOT NULL PRIMARY KEY CHECK (ci <= 99999999), -- PK
    
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    telefono_contacto VARCHAR(20) NOT NULL, -- Al menos el teléfono como información de contacto.
	correo_contacto VARCHAR(40) CHECK (correo_contacto LIKE '%@%')
);

CREATE TABLE INSTRUCTORES (
	ci INTEGER UNSIGNED NOT NULL PRIMARY KEY CHECK (ci <= 99999999), -- PK
    
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    telefono_contacto VARCHAR(20) NOT NULL, -- Al menos el teléfono como información de contacto.
	correo_contacto VARCHAR(40) CHECK (correo_contacto LIKE '%@%')
);

CREATE TABLE LOGIN (
	correo VARCHAR(40) NOT NULL PRIMARY KEY CHECK (correo LIKE '%@%'), -- PK
    
    contrasena VARCHAR(40) NOT NULL
);

CREATE TABLE CLASES (
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, -- PK
    
    ci_instructor INTEGER UNSIGNED NOT NULL CHECK (ci_instructor <= 99999999),
    id_turno TINYINT UNSIGNED NOT NULL,
    id_actividad TINYINT UNSIGNED NOT NULL,
    dictada BOOL NOT NULL,
    
    FOREIGN KEY (ci_instructor) REFERENCES INSTRUCTORES(ci), -- FK1
    FOREIGN KEY (id_turno) REFERENCES TURNOS(id), -- FK2
    FOREIGN KEY (id_actividad) REFERENCES ACTIVIDADES(id) -- FK3
);

CREATE TABLE EQUIPAMIENTOS (
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, -- PK
    
    id_actividad TINYINT UNSIGNED NOT NULL,
	descripcion VARCHAR(100) NOT NULL,
    costo MEDIUMINT UNSIGNED NOT NULL,
    
    FOREIGN KEY (id_actividad) REFERENCES ACTIVIDADES(id) -- FK
);

CREATE TABLE ALUMNOS_CLASES (
	id_clase TINYINT UNSIGNED NOT NULL,
    ci_alumno INTEGER UNSIGNED NOT NULL CHECK (ci_alumno <= 99999999),
    id_equipamiento TINYINT UNSIGNED NOT NULL,
    
    PRIMARY KEY (id_clase, ci_alumno, id_equipamiento),  -- Clave primaria compuesta

    FOREIGN KEY (id_clase) REFERENCES CLASES(id), -- FK1
    FOREIGN KEY (ci_alumno) REFERENCES ALUMNOS(ci), -- FK2
    FOREIGN KEY (id_equipamiento) REFERENCES EQUIPAMIENTOS(id) -- FK3
);