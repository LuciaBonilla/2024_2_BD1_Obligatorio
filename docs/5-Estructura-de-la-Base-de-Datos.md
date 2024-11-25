# Estructura de la Base de Datos

La base de datos es de MySQL y cuenta con 8 tablas, las cuales se ven específicamente en el [archivo de creación de tablas](../scripts/1_create-tables.sql) que se ejecuta al encender por primera vez el contenedor Docker con la base de datos. Estas tablas se representan en este [diagrama](diagrams/TablasBaseDeDatos.png).

La configuración `ON DELETE CASCADE` sobre las claves forráneas al crear las tablas especifica que, si se elimina un registro de la tabla padre (la tabla referenciada), automáticamente se eliminarán también todos los registros relacionados en la tabla hija (la tabla que contiene la clave foránea). Esto mantiene la consistencia de datos, automatiza la eliminación y simplifica el mantenimiento.

Nota: La tabla `LOGIN` no se relaciona con niguna otra, ya que sólo representa cuentas de administradores para poder interactuar con el backend, es decir, si se encuentra un registro con el correo y contraseña proporcionados por el usuario, entonces el usuario puede interactuar con la base de datos a través del backend.