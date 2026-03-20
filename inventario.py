import sqlite3

# ----------------------------------
# COLORAMA (OPCIONAL)
# ----------------------------------
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False


# ----------------------------------
# CONEXIÓN Y CREACIÓN DE LA BASE
# ----------------------------------
def conectar_db():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )
    """)

    conexion.commit()
    return conexion


# ----------------------------------
# REGISTRAR PRODUCTO
# ----------------------------------
def registrar_producto(conexion):
    cursor = conexion.cursor()

    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("❌ El nombre no puede estar vacío")
        return

    descripcion = input("Descripción: ").strip()

    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
    except ValueError:
        print("❌ Cantidad y precio deben ser números")
        return

    categoria = input("Categoría: ").strip()

    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))

    conexion.commit()
    print("✅ Producto registrado correctamente")


# ----------------------------------
# MOSTRAR PRODUCTOS
# ----------------------------------
def mostrar_productos(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if not productos:
        print("📭 No hay productos registrados")
        return

    print("\n📦 LISTA DE PRODUCTOS")
    for prod in productos:
        print(f"""
ID: {prod[0]}
Nombre: {prod[1]}
Descripción: {prod[2]}
Cantidad: {prod[3]}
Precio: ${prod[4]}
Categoría: {prod[5]}
-------------------------
        """)


# ----------------------------------
# BUSCAR PRODUCTO POR ID
# ----------------------------------
def buscar_producto(conexion):
    cursor = conexion.cursor()

    try:
        id_producto = int(input("Ingrese el ID del producto: "))
    except ValueError:
        print("❌ ID inválido")
        return

    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    if producto:
        print(f"""
🔍 PRODUCTO ENCONTRADO
ID: {producto[0]}
Nombre: {producto[1]}
Descripción: {producto[2]}
Cantidad: {producto[3]}
Precio: ${producto[4]}
Categoría: {producto[5]}
        """)
    else:
        print("❌ No se encontró un producto con ese ID")


# ----------------------------------
# ACTUALIZAR PRODUCTO
# ----------------------------------
def actualizar_producto(conexion):
    cursor = conexion.cursor()

    try:
        id_producto = int(input("ID del producto a actualizar: "))
    except ValueError:
        print("❌ ID inválido")
        return

    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    if not cursor.fetchone():
        print("❌ Producto no encontrado")
        return

    nombre = input("Nuevo nombre: ").strip()
    descripcion = input("Nueva descripción: ").strip()

    try:
        cantidad = int(input("Nueva cantidad: "))
        precio = float(input("Nuevo precio: "))
    except ValueError:
        print("❌ Cantidad o precio inválido")
        return

    categoria = input("Nueva categoría: ").strip()

    cursor.execute("""
        UPDATE productos
        SET nombre=?, descripcion=?, cantidad=?, precio=?, categoria=?
        WHERE id=?
    """, (nombre, descripcion, cantidad, precio, categoria, id_producto))

    conexion.commit()
    print("✅ Producto actualizado correctamente")


# ----------------------------------
# ELIMINAR PRODUCTO
# ----------------------------------
def eliminar_producto(conexion):
    cursor = conexion.cursor()

    try:
        id_producto = int(input("ID del producto a eliminar: "))
    except ValueError:
        print("❌ ID inválido")
        return

    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conexion.commit()

    if cursor.rowcount > 0:
        print("🗑️ Producto eliminado")
    else:
        print("❌ No se encontró el producto")


# ----------------------------------
# REPORTE DE BAJO STOCK
# ----------------------------------
def reporte_bajo_stock(conexion):
    cursor = conexion.cursor()

    try:
        limite = int(input("Mostrar productos con cantidad menor o igual a: "))
    except ValueError:
        print("❌ Valor inválido")
        return

    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()

    if not productos:
        print("✅ No hay productos con bajo stock")
        return

    print("\n⚠️ PRODUCTOS CON BAJO STOCK")
    for prod in productos:
        print(f"{prod[1]} | Cantidad: {prod[3]}")


# ----------------------------------
# CARGAR DATOS DE PRUEBA
# ----------------------------------
def cargar_datos_prueba(conexion):
    cursor = conexion.cursor()

    productos = [
        ("Yerba", "Yerba mate tradicional", 5, 2500, "Alimentos"),
        ("Azúcar", "Azúcar blanca 1kg", 2, 1200, "Alimentos"),
        ("Fideos", "Fideos spaghetti", 10, 900, "Alimentos"),
        ("Lavandina", "Lavandina 1L", 1, 800, "Limpieza"),
        ("Detergente", "Detergente líquido", 3, 1100, "Limpieza")
    ]

    cursor.executemany("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, productos)

    conexion.commit()
    print("✔ Datos de prueba cargados correctamente")


# ----------------------------------
# MENÚ
# ----------------------------------
def menu():
    print("""
==============================
📦 SISTEMA DE INVENTARIO
==============================
1. Registrar producto
2. Mostrar productos
3. Buscar producto por ID
4. Actualizar producto
5. Eliminar producto
6. Reporte de bajo stock
7. Cargar datos de prueba
0. Salir
==============================
    """)


# ----------------------------------
# PROGRAMA PRINCIPAL
# ----------------------------------
def main():
    conexion = conectar_db()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(conexion)
        elif opcion == "2":
            mostrar_productos(conexion)
        elif opcion == "3":
            buscar_producto(conexion)
        elif opcion == "4":
            actualizar_producto(conexion)
        elif opcion == "5":
            eliminar_producto(conexion)
        elif opcion == "6":
            reporte_bajo_stock(conexion)
        elif opcion == "7":
            cargar_datos_prueba(conexion)
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida")

    conexion.close()


# ----------------------------------
# EJECUCIÓN
# ----------------------------------
main()

