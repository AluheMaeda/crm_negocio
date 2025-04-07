from db import crear_conexion


def agregar_cuenta(cliente_email, tipo, saldo_inicial=0.0):
    conn = crear_conexion()
    cursor = conn.cursor()

    # Obtener cliente por email
    cursor.execute("SELECT id FROM clientes WHERE email = ?", (cliente_email,))
    resultado = cursor.fetchone()

    if not resultado:
        print("❌ Error: Cliente no encontrado.")
        conn.close()
        return

    cliente_id = resultado[0]

    cursor.execute('''
        INSERT INTO cuentas (cliente_id, tipo, saldo)
        VALUES (?, ?, ?)
    ''', (cliente_id, tipo, saldo_inicial))

    conn.commit()
    conn.close()
    print(f"✅ Cuenta '{tipo}' creada para el cliente con email '{cliente_email}'")


def ver_cuentas():
    conn = crear_conexion()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT cuentas.id, clientes.nombre, cuentas.tipo, cuentas.saldo
        FROM cuentas
        JOIN clientes ON cuentas.cliente_id = clientes.id
    ''')

    cuentas = cursor.fetchall()
    print("📋 Todas las cuentas registradas:")
    for c in cuentas:
        print(f"ID: {c[0]}, Cliente: {c[1]}, Tipo: {c[2]}, Saldo: ${c[3]:,.2f}")

    conn.close()


def ver_cuentas_cliente(email):
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
        SELECT id, tipo, saldo FROM cuentas
        WHERE cliente_id = ?
    ''', (cliente_id,))
    cuentas = cursor.fetchall()

    if not cuentas:
        print(f"ℹ️ El cliente '{nombre}' no tiene cuentas registradas.")
    else:
        print(f"📋 Cuentas del cliente '{nombre}':")
        for c in cuentas:
            print(f"ID: {c[0]}, Tipo: {c[1]}, Saldo: ${c[2]:,.2f}")

    conn.close()

def editar_cuenta(cuenta_id, nuevo_tipo=None, nuevo_saldo=None):
    from db import crear_conexion
    conn = crear_conexion()
    cursor = conn.cursor()

    # Verificar si la cuenta existe
    cursor.execute("SELECT tipo, saldo FROM cuentas WHERE id = ?", (cuenta_id,))
    cuenta = cursor.fetchone()

    if not cuenta:
        print("❌ Error: Cuenta no encontrada.")
        conn.close()
        return

    tipo_actual, saldo_actual = cuenta
    nuevo_tipo = nuevo_tipo if nuevo_tipo else tipo_actual
    nuevo_saldo = nuevo_saldo if nuevo_saldo is not None else saldo_actual

    cursor.execute('''
        UPDATE cuentas SET tipo = ?, saldo = ? WHERE id = ?
    ''', (nuevo_tipo, nuevo_saldo, cuenta_id))
    conn.commit()
    conn.close()
    print(f"✅ Cuenta ID {cuenta_id} actualizada correctamente.")

def eliminar_cuenta(cuenta_id):
    from db import crear_conexion
    conn = crear_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cuentas WHERE id = ?", (cuenta_id,))
    cuenta = cursor.fetchone()

    if not cuenta:
        print("❌ Error: No se encontró la cuenta.")
        conn.close()
        return

    cursor.execute("DELETE FROM cuentas WHERE id = ?", (cuenta_id,))
    conn.commit()
    conn.close()
    print(f"🗑️ Cuenta ID {cuenta_id} eliminada exitosamente.")
