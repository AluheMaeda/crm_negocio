import sqlite3
from db import crear_conexion

def registrar_venta(cliente_email, producto, monto, fecha):
    conn = crear_conexion()
    cursor = conn.cursor()

    # Obtener cliente_id
    cursor.execute("SELECT id FROM clientes WHERE email = ?", (cliente_email,))
    resultado = cursor.fetchone()

    if not resultado:
        print("❌ Error: Cliente no encontrado.")
        conn.close()
        return

    cliente_id = resultado[0]

    cursor.execute('''
        INSERT INTO ventas (cliente_id, producto, monto, fecha)
        VALUES (?, ?, ?, ?)
    ''', (cliente_id, producto, monto, fecha))

    conn.commit()
    conn.close()
    print(f"✅ Venta registrada para el cliente '{cliente_email}'.")

def ver_ventas():
    conn = crear_conexion()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT ventas.id, clientes.nombre, ventas.producto, ventas.monto, ventas.fecha
        FROM ventas
        JOIN clientes ON ventas.cliente_id = clientes.id
    ''')

    ventas = cursor.fetchall()
    if not ventas:
        print("ℹ️ No hay ventas registradas.")
    else:
        print("📋 Lista de todas las ventas:")
        for v in ventas:
            print(f"ID: {v[0]}, Cliente: {v[1]}, Producto: {v[2]}, Monto: ${v[3]:,.2f}, Fecha: {v[4]}")

    conn.close()

def ver_ventas_cliente(email):
    conn = crear_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre FROM clientes WHERE email = ?", (email,))
    cliente = cursor.fetchone()

    if not cliente:
        print("❌ Error: Cliente no encontrado.")
        conn.close()
        return

    cliente_id, nombre = cliente

    cursor.execute('''
        SELECT producto, monto, fecha FROM ventas
        WHERE cliente_id = ?
    ''', (cliente_id,))

    ventas = cursor.fetchall()

    if not ventas:
        print(f"ℹ️ El cliente '{nombre}' no tiene ventas registradas.")
    else:
        print(f"📋 Ventas del cliente '{nombre}':")
        for v in ventas:
            print(f"Producto: {v[0]}, Monto: ${v[1]:,.2f}, Fecha: {v[2]}")

    conn.close()
