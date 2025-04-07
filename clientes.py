import sqlite3
import db  # Importamos para usar crear_conexion y ver_clientes
import csv

def agregar_cliente(nombre, email, telefono):
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    nombre = nombre.title()
    cursor.execute("SELECT * FROM clientes WHERE email = ?", (email,))
    if cursor.fetchone():
        print("❌ Error: El email ya está registrado.")
        conn.close()
        return

    cursor.execute('''
        INSERT INTO clientes (nombre, email, telefono)
        VALUES (?, ?, ?)
    ''', (nombre, email, telefono))

    conn.commit()
    conn.close()
    print("✅ Cliente agregado correctamente.")

def editar_cliente(email, nuevo_nombre=None, nuevo_telefono=None):
    clientes = db.ver_clientes()
    cliente_existente = [c for c in clientes if c[2] == email]
    
    nuevo_nombre = nuevo_nombre.title()
    if not cliente_existente:
        print("❌ Error: No se encontró un cliente con ese email.")
        return
    
    cliente = cliente_existente[0]
    nuevo_nombre = nuevo_nombre if nuevo_nombre else cliente[1]
    nuevo_telefono = nuevo_telefono if nuevo_telefono else cliente[3]
    
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE clientes SET nombre = ?, telefono = ? WHERE email = ?
    ''', (nuevo_nombre, nuevo_telefono, email))
    conn.commit()
    conn.close()
    print("✅ Cliente editado correctamente.")

def eliminar_cliente(email):
    conexion = db.crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes WHERE email = ?", (email,))
    cliente = cursor.fetchone()
    
    if cliente:
        cursor.execute("DELETE FROM clientes WHERE email = ?", (email,))
        conexion.commit()
        print(f"🗑️ Cliente con email '{email}' eliminado.")
    else:
        print("❌ Error: Cliente no encontrado.")
    
    conexion.close()

def exportar_clientes_csv(ruta_archivo):
    from db import crear_conexion
    conn = crear_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, email, telefono FROM clientes")
    clientes = cursor.fetchall()

    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["ID", "Nombre", "Email", "Teléfono"])  # Encabezado
        writer.writerows(clientes)

    conn.close()
    print(f"✅ Clientes exportados a '{ruta_archivo}'")

def exportar_cuentas_csv(ruta_archivo):
    from db import crear_conexion
    conn = crear_conexion()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT cuentas.id, clientes.nombre, cuentas.tipo, cuentas.saldo
        FROM cuentas
        JOIN clientes ON cuentas.cliente_id = clientes.id
    ''')
    cuentas = cursor.fetchall()

    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["ID Cuenta", "Nombre Cliente", "Tipo", "Saldo"])  # Encabezado
        writer.writerows(cuentas)

    conn.close()
    print(f"✅ Cuentas exportadas a '{ruta_archivo}'")

def transferir(cuenta_origen_id, cuenta_destino_id, monto):
    from db import crear_conexion
    conn = crear_conexion()
    cursor = conn.cursor()

    # Verificar existencia de cuentas
    cursor.execute("SELECT saldo FROM cuentas WHERE id = ?", (cuenta_origen_id,))
    origen = cursor.fetchone()
    cursor.execute("SELECT saldo FROM cuentas WHERE id = ?", (cuenta_destino_id,))
    destino = cursor.fetchone()

    if not origen or not destino:
        print("❌ Error: Una o ambas cuentas no existen.")
        conn.close()
        return

    saldo_origen = origen[0]

    # Verificar saldo suficiente
    if saldo_origen < monto:
        print("❌ Error: Saldo insuficiente en la cuenta de origen.")
        conn.close()
        return

    # Realizar transferencia
    cursor.execute("UPDATE cuentas SET saldo = saldo - ? WHERE id = ?", (monto, cuenta_origen_id))
    cursor.execute("UPDATE cuentas SET saldo = saldo + ? WHERE id = ?", (monto, cuenta_destino_id))
    conn.commit()
    conn.close()
    print(f"✅ Transferencia de ${monto:,.2f} realizada de cuenta {cuenta_origen_id} a cuenta {cuenta_destino_id}.")

#Ver clientes
def ver_clientes():
    conn = db.crear_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes
