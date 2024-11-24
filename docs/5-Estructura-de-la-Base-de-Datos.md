# Estructura de la Base de Datos

La base de datos es de MySQL y cuenta con 8 tablas, las cuales se ven específicamente en el [archivo de creación de tablas](../scripts/1_create-tables.sql) que se ejecuta al encender el contenedor Docker con la base de datos.

Las tablas se representan en este [diagrama](diagrams/TablasBaseDeDatos.png).

Nota: La tabla LOGIN no se relaciona con niguna otra, ya que sólo representa cuentas de administradores para poder interactuar con el backend, es decir, si se encuentra un registro con el correo y contraseña proporcionados por el usuario, entonces el usuario puede interactuar con la base de datos a través del backend.