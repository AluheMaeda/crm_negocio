import csv
from db import crear_conexion
from cuentas import agregar_cuenta

def importar_clientes(nombre_archivo="data/clientes.csv"):
    conn = crear_conexion()
    cursor = conn.cursor()

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            try:
                cursor.execute('''
                    INSERT OR IGNORE INTO clientes (nombre, email, telefono)
                    VALUES (?, ?, ?)
                ''', (fila["Nombre"].strip().title(), fila["Email"].strip(), fila["Teléfono"].strip()))
            except Exception as e:
                print(f"❌ Error al importar cliente {fila}: {e}")

    conn.commit()
    conn.close()
    print(f"✅ Clientes importados desde {nombre_archivo}")


def importar_cuentas(nombre_archivo="data/cuentas.csv"):
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            try:
                email = fila["Cliente"].strip().lower()
                tipo = fila["Tipo"].strip()
                saldo = float(fila["Saldo"])
                agregar_cuenta(email, tipo, saldo)
            except Exception as e:
                print(f"❌ Error al importar cuenta {fila}: {e}")

    print(f"✅ Cuentas importadas desde {nombre_archivo}")


def importar_ventas(nombre_archivo="data/ventas.csv"):
    conn = crear_conexion()
    cursor = conn.cursor()

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            try:
                email = fila["Cliente"].strip().lower()
                cursor.execute("SELECT id FROM clientes WHERE email = ?", (email,))
                cliente = cursor.fetchone()
                if cliente:
                    cliente_id = cliente[0]
                    cursor.execute('''
                        INSERT INTO ventas (cliente_id, producto, monto, fecha)
                        VALUES (?, ?, ?, ?)
                    ''', (cliente_id, fila["Producto"], fila["Monto"], fila["Fecha"]))
            except Exception as e:
                print(f"❌ Error al importar venta {fila}: {e}")

    conn.commit()
    conn.close()
    print(f"✅ Ventas importadas desde {nombre_archivo}")


def importar_datos_csv():
    importar_clientes()
    importar_cuentas()
    importar_ventas()
