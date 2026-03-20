SISTEMA DE INVENTARIO EN PYTHON

Este proyecto es un programa en Python que permite gestionar un inventario
de productos usando una base de datos SQLite.

La aplicación funciona por consola y se maneja a través de un menú, lo que
permite realizar todas las operaciones básicas sobre los productos de forma
sencilla.

------------------------------------
FUNCIONALIDADES
------------------------------------

Con el sistema se puede:
- Cargar productos nuevos
- Ver todos los productos registrados
- Buscar productos por su ID
- Modificar datos de un producto
- Eliminar productos del inventario
- Ver productos con bajo stock
- Cargar datos de prueba para testear el funcionamiento

------------------------------------
BASE DE DATOS
------------------------------------

El programa utiliza una base de datos llamada "inventario.db", que se crea
automáticamente al ejecutar el archivo por primera vez.

Los datos que se guardan de cada producto son:
- ID
- Nombre
- Descripción
- Cantidad
- Precio
- Categoría

------------------------------------
EJECUCIÓN
------------------------------------

Para ejecutar el programa:
1. Abrir una terminal en la carpeta del proyecto
2. Ejecutar el comando:

   python inventario.py

3. Usar el menú para interactuar con el sistema

------------------------------------
ACLARACIÓN
------------------------------------

La opción de cargar datos de prueba se agregó para facilitar la corrección y
la prueba del sistema, sin necesidad de ingresar productos manualmente.
