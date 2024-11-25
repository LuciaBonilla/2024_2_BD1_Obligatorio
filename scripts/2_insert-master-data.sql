USE ucu_snow_sports;

-- Formato de hora: HH:MM:SS
INSERT INTO TURNOS(hora_inicio, hora_fin)
VALUES
("09:00:00", "11:00:00"),
("12:00:00", "14:00:00"),
("16:00:00", "18:00:00");

INSERT INTO ACTIVIDADES(nombre, descripcion, costo, edad_minima)
VALUES
("Snowboard", "Deporte de deslizamiento sobre nieve con tabla", 5000, 12),
("Ski", "Deporte de deslizamiento sobre nieve con esquís", 4500, 15),
("Moto de Nieve", "Actividad de conducción de motos en nieve", 8000, 18);

INSERT INTO EQUIPAMIENTOS(id_actividad, descripcion, costo)
VALUES
((SELECT id FROM ACTIVIDADES WHERE nombre="Snowboard"), "Tabla de snowboard", 3000),
((SELECT id FROM ACTIVIDADES WHERE nombre="Snowboard"), "Botas de snowboard", 1500),
((SELECT id FROM ACTIVIDADES WHERE nombre="Snowboard"), "Casco para snowboard", 800),
((SELECT id FROM ACTIVIDADES WHERE nombre="Ski"), "Esquís", 2500),
((SELECT id FROM ACTIVIDADES WHERE nombre="Ski"), "Botas de esquí", 1200),
((SELECT id FROM ACTIVIDADES WHERE nombre="Ski"), "Bastones para esquí", 500),
((SELECT id FROM ACTIVIDADES WHERE nombre="Ski"), "Antiparras para esquí", 700),
((SELECT id FROM ACTIVIDADES WHERE nombre="Moto de Nieve"), "Casco para moto de nieve", 1000),
((SELECT id FROM ACTIVIDADES WHERE nombre="Moto de Nieve"), "Traje térmico para moto de nieve", 3500);

INSERT INTO LOGIN(correo, contrasena)
VALUES
("admin@mail.com", "123");

-- Insert dummy data for ALUMNOS
INSERT INTO ALUMNOS(ci, nombre, apellido, fecha_nacimiento, telefono_contacto, correo_contacto)
VALUES
(12345678, "Juan", "Perez", "2000-01-01", "123456789", "juan.perez@mail.com"),
(23456789, "Maria", "Gomez", "1998-05-15", "987654321", "maria.gomez@mail.com"),
(34567890, "Carlos", "Lopez", "2002-07-20", "456789123", "carlos.lopez@mail.com"),
(45678901, "Ana", "Martinez", "1999-11-30", "789123456", "ana.martinez@mail.com"),
(56789012, "Luis", "Garcia", "2001-03-25", "321654987", "luis.garcia@mail.com");

-- Insert dummy data for INSTRUCTORES
INSERT INTO INSTRUCTORES(ci, nombre, apellido, telefono_contacto, correo_contacto)
VALUES
(87654321, "Pedro", "Fernandez", "123123123", "pedro.fernandez@mail.com"),
(76543210, "Laura", "Rodriguez", "321321321", "laura.rodriguez@mail.com"),
(65432109, "Miguel", "Sanchez", "456456456", "miguel.sanchez@mail.com"),
(54321098, "Sofia", "Ramirez", "789789789", "sofia.ramirez@mail.com"),
(43210987, "Diego", "Torres", "987987987", "diego.torres@mail.com");

-- Insert dummy data for CLASES
INSERT INTO CLASES(ci_instructor, id_turno, id_actividad, dictada)
VALUES
(87654321, 1, (SELECT id FROM ACTIVIDADES WHERE nombre="Snowboard"), TRUE),
(76543210, 2, (SELECT id FROM ACTIVIDADES WHERE nombre="Ski"), TRUE),
(65432109, 3, (SELECT id FROM ACTIVIDADES WHERE nombre="Moto de Nieve"), FALSE),
(54321098, 1, (SELECT id FROM ACTIVIDADES WHERE nombre="Ski"), TRUE),
(43210987, 2, (SELECT id FROM ACTIVIDADES WHERE nombre="Snowboard"), FALSE);

-- Insert dummy data for ALUMNOS_CLASES
INSERT INTO ALUMNOS_CLASES(id_clase, ci_alumno, id_equipamiento)
VALUES
((SELECT id FROM CLASES WHERE ci_instructor=87654321 AND id_turno=1), 12345678, (SELECT id FROM EQUIPAMIENTOS WHERE descripcion="Tabla de snowboard")),
((SELECT id FROM CLASES WHERE ci_instructor=76543210 AND id_turno=2), 23456789, (SELECT id FROM EQUIPAMIENTOS WHERE descripcion="Esquís")),
((SELECT id FROM CLASES WHERE ci_instructor=65432109 AND id_turno=3), 34567890, (SELECT id FROM EQUIPAMIENTOS WHERE descripcion="Casco para moto de nieve")),
((SELECT id FROM CLASES WHERE ci_instructor=54321098 AND id_turno=1), 45678901, (SELECT id FROM EQUIPAMIENTOS WHERE descripcion="Botas de esquí")),
((SELECT id FROM CLASES WHERE ci_instructor=43210987 AND id_turno=2), 56789012, (SELECT id FROM EQUIPAMIENTOS WHERE descripcion="Botas de snowboard"));