# Código Fuente de Backend y Frontend

Se utiliza monorepo para todo el proyecto, en este se tiene el backend y el frontend; se usa Docker para iniciar todo.

## Backend

- El [backend](../backend/src/) está realizado con `Python` y utiliza `Flask`, un framework web que es un módulo de Python que permite desarrollar aplicaciones web de forma sencilla.

- Sigue el patrón de arquitectura de software MVC antes mencionado.

- Sigue fuertemente el principio fundamental de la programación orientada a objetos: Principio de responsabilidad única.

`Definición: Una clase debe tener solo una razón para cambiar, lo que significa que debe tener solo un trabajo o responsabilidad.`

Este enfoque ha ayudado a mantener el código e irlo escalando durante la creación del proyecto.

`Nota:` Ver los comentarios del código fuente, ya que indican de manera precisa qué hace cada clase y método del código.

- Utiliza `mysql-connector`, una biblioteca oficial desarrollada por MySQL para permitir que aplicaciones escritas en Python interactúen con bases de datos MySQL. Ofrece una interfaz para conectarse a servidores MySQL y ejecutar consultas SQL de manera programática.

Algo muy interesante es que `mysql-connector` permite evitar la inyección SQL, es decir, insertar código SQL malicioso por medio de las entradas de usuario. En la práctica, utilizando placeholders `%s` y pasando los datos de entrada como una tupla, se asegura que cualquier entrada proporcionada por el usuario sea tratada como datos literales, no como parte del código SQL ejecutable.

Ejemplo: entrada de usuario: `Gifts'--`

Script MySQL con concatenación normal de strings:

`SELECT * FROM products WHERE category = 'Gifts'-- AND released = 1` -> Da todos los productos lanzados y no lanzados.

Script MySQL con placeholders:

`SELECT * FROM products WHERE category = %s AND released = 1` -> Script  dado a `my-sql-connector` junto al valor de la entrada del usuario pata que la inyecte de forma segura.

Script MySQL que se termina ejecutando:

`SELECT * FROM products WHERE category = 'Gifts\'--' AND released = 1;` -> La barra indica que `'` es parte de la cadena literal. Da todos los productos lanzados.

## Frontend

- El [frontend](../frontend/ucu-web/) fue construido con Vite: una herramienta de desarrollo que tiene como objetivo proporcionar una experiencia de desarrollo más rápida y sencilla para proyectos web modernos.

- Utiliza la librería `React` que simplifica la creación de interfaces de usuario a través de la creación de componentes que representan una parte de la interfaz, lo cual usa enormemente los paradigmas de la programación orientada a objetos.