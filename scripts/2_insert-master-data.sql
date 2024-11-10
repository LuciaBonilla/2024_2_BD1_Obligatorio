USE ucu_snow_sports;

-- Formato de hora: HH:MM:SS
INSERT INTO TURNOS(hora_inicio, hora_fin)
VALUES
("09:00:00", "11:00:00"),
("12:00:00", "14:00:00"),
("16:00:00","18:00:00");

INSERT INTO ACTIVIDADES(nombre, descripcion, costo, edad_minima)
VALUES
("Snowboard", "Deporte de deslizamiento sobre nieve con tabla", 5000, 12),
("Ski", "Deporte de deslizamiento sobre nieve con esquís", 4500, 15),
("Moto de Nieve", "Actividad de conducción de motos en nieve", 8000, 18);

INSERT INTO EQUIPAMIENTOS (id_actividad, descripcion, costo)
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