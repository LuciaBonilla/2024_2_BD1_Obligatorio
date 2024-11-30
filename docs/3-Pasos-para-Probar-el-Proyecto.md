# Pasos Para Probar el Proyecto

1. Sobre el directorio raíz ejecutar:
   - `docker-compose build`
   - `docker-compose up`

Esto levantará por primera vez los contenedores Docker, específicamente, levantará un contenedor con la base de datos, luego otro contenedor con el backend y, finalmente, el que contiene el frontend.

`Nota:` Se recomienda utilizar `docker-compose -d` para que sea detach (ejecución en segundo plano), y luego `docker-compose down {id del contenedor a apagar}` para asegurar que se apaga el contenedor de manera correcta.

2. Luego de levantados los contenedores, ir a la ruta principal del frontend (http://localhost:5173) para probar la app como un usuario normal, pero si el frontend no funciona, entonces ver la sección [6-Endpoints](./6-Endpoints.md) para probar el backend mediante otra herramienta.

`Nota:` Para hacer reload del proyecto se puede usar `docker-compose up -d --build --force-recreate`, pero tener en cuenta que no se volverán a ejecutar los [scripts MySQL definidos](../scripts/) al levantar la base de datos por primera vez y que los datos persistidos no se borrarán.