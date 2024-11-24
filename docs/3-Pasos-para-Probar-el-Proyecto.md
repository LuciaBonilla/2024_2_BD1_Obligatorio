# Pasos Para Probar los Servicios

1. Sobre el directorio raíz ejecutar:
   - `docker-compose build`
   - `docker-compose up`

Esto levantará por primera vez los contenedores Docker, específicamente, levantará un contenedor con la base de datos, luego otro contenedor con el backend y, finalemnte, el que contiene el frontend.

Nota: Se recomienda utilizar `docker-compose -d` para que sea detach, y luego `docker-compose down {id del contenedor a apagar}` para asegurar que se apaga el contenedor de manera correcta.

2. Luego de levantados los contenedores, ir a la ruta principal del frontend (http://localhost:5173).

3. Para hacer reload del projecto se puede usar `docker-compose up -d --build --force-recreate`, pero tener en cuenta que no se volverán a ejecutar los [scripts MySQL definidos](../scripts/) al levantar la base de datos por primera vez.