# Conclusiones del Proyecto

1. El sistema propuesto satisface las necesidades básicas de gestión de la nueva escuela de deportes de nieve de la UCU.

La implementación permitió un manejo eficaz de:

- alumnos,
- instructores,
- actividades,
- turnos,
- equipamientos,
- clases,
- asistencias,

asegurando el cumplimiento de las reglas establecidas para las clases y la seguridad de los datos. Además, las funcionalidades de reporte ofrecen herramientas para evaluar el desempeño de la escuela.

2. El equipo aprendió e implementó de forma básica herramientas tecnológicas y patrones de diseño comunes en el desarrollo de software.

- Cumplimiento del Patrón MVC: Aunque no es una implementación completamente estricta, la separación de responsabilidades entre el Modelo, la Vista y el Controlador aseguró un diseño limpio y escalable.

- Dockerización: La utilización de Docker y Docker Compose simplificó el despliegue, facilitó la reproducción del entorno de desarrollo y redució problemas relacionados con diferencias en entornos.

La arquitectura basada en contenedores simplificó el proceso de desarrollo, asegurando consistencia entre entornos y facilitando la integración continua. Esto reduce los costos asociados a errores de configuración y permite escalar los servicios independientemente.

- Seguridad: Se implementaron medidas básicas de seguridad como la prevención de inyección SQL y autenticación de administradores para proteger los datos.

- Estandarización y Modularidad: El uso de herramientas modernas como Flask para el backend y React para el frontend aseguró un desarrollo organizado y la posibilidad de futuras expansiones.

3. Las limiticiones identificadas fueron:

- Implementación de Seguridad: Aunque se implementaron mecanismos básicos, el envío de credenciales en cada solicitud no es óptimo. Migrar a un sistema basado en tokens, como JWT, sería una mejora significativa.

- Estado del Frontend: Varias páginas y funcionalidades clave del frontend no están completadas, limitando la experiencia de usuario y el alcance de la solución actual.

- Dependencia del Backend: La falta de una interfaz gráfica completamente funcional obligó a depender de herramientas como Postman para probar ciertas funcionalidades.

- Dificultad en Desarrollo Frontend: Las respuestas poco informativas del backend pueden ser engorrosas para el desarrollo frontend, ya que se requiere realizar más consultas para obtener cierta información que se podría haber entregado en una sola llamada al backend.

4. Flexibilidad y Escalabilidad

- El diseño del sistema permitió consultar, agregar, editar y eliminar entidades de la escuela (alumnos, instructores, etc.) sin alterar significativamente la estructura existente.

- Los tipos de datos elegidos al crear las tablas permitieron reducir la memoria desperdiciada, garantizar que los valores almacenados cumplan con un formato y rango esperado, y prevenir errores de conversión y validación de datos. Estos ítems son cruciales para la escabilidad futura del sistema.

- Además, los reportes permitieron consultar datos para evaluar si el sistema debe escalar a futuro.