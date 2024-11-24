# Uso del Patrón de Arquitectura de Software (MVC - Modelo–Vista–Controlador)

En nuestro proyecto, implementamos el patrón de arquitectura MVC (Modelo-Vista-Controlador), cuyo objetivo es separar las responsabilidades en tres componentes principales. Esto facilita el mantenimiento, escalabilidad y reutilización del código.

Nota: Tener en cuenta que nuestra arquitectura no es 100% acorde al patrón MVC, es decir, se personalizó la arquitectura para mayor facilidad.

Los componentes de nuestro proyecto son:

1. Modelo (Model)

El Modelo representa la lógica de negocio de la aplicación y es responsable de gestionar los datos. Además, implementa las reglas de negocio y maneja la interacción con la base de datos.

Responsabilidades:
- Gestionar los datos de la aplicación.
- Implementar la lógica y reglas de negocio necesarias.

Acciones:
- Realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
- Interactuar con la base de datos para obtener o modificar información.

Localización:
- En el backend del proyecto.

2. Controlador (Controller)

El Controlador actúa como intermediario entre el frontend (Vista) y el Modelo. Recibe las solicitudes realizadas por la Vista, interactúa con el Modelo si es necesario y devuelve una respuesta en formato JSON al cliente. El Controlador no gestiona la presentación de los datos; su propósito es exclusivamente procesar solicitudes y estructurar respuestas.

Responsabilidades:
- Procesar las solicitudes del frontend (por ejemplo, peticiones HTTP).
- Interactuar con el Modelo para recuperar o modificar datos.
- Responder al frontend con datos en formato JSON.

Acciones:
- Validar y procesar las entradas del usuario o del cliente.
- Controlar la lógica del flujo de la aplicación.
- Enviar respuestas estructuradas (JSON) al frontend para que sean procesadas y presentadas.

Localización:
- En el backend del proyecto.

3. Vista (View)

La Vista corresponde al frontend de la aplicación. Su responsabilidad principal es interactuar con el usuario final y mostrar los datos obtenidos del backend. En este proyecto, la Vista realiza llamadas al Controlador a través de una API para obtener datos en formato JSON, los cuales procesa y presenta al usuario mediante una interfaz gráfica.

Responsabilidades:
- Presentar los datos al usuario de manera adecuada e interactiva.
- Proporcionar una interfaz intuitiva para la interacción del usuario.

Acciones:
- Realizar solicitudes al backend (Controlador y Modelo) mediante HTTP (por ejemplo, usando fetch o axios).
- Recibir y procesar datos en formato JSON proporcionados por el backend.
- Renderizar la interfaz de usuario con la información obtenida.

Localización:
- En el frontend del proyecto.

## Resumen del Flujo MVC en el Proyecto

1. Frontend (Vista): Realiza una solicitud al backend a través del Controlador (por ejemplo, una petición GET o POST).

2. Backend (Controlador y Modelo): El Controlador procesa la solicitud, valida los datos, interactúa con el Modelo (el cual interactúa con la base de datos) si es necesario y genera una respuesta en formato JSON.

3. Frontend (Vista): Recibe la respuesta JSON del backend, procesa los datos y los presenta al usuario mediante la interfaz visual.

Este enfoque asegura una separación clara de responsabilidades:

- El frontend (Vista) se concentra exclusivamente en la presentación y experiencia del usuario.
- El backend (Modelo y Controlador) maneja la lógica de negocio y la gestión de datos.