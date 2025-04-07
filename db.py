import sqlite3

# Nombre del archivo de la base de datos
DB_NAME = "data/crm.db"

def crear_conexion():
    return sqlite3.connect(DB_NAME)

def crear_tablas():
    conexion = crear_conexion()
    cursor = conexion.cursor()

    # Crear tabla de clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telefono TEXT
        )
    ''')

    # Crear tabla de cuentas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cuentas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            tipo TEXT NOT NULL,
            saldo REAL DEFAULT 0.0,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    ''')

    # Crear tabla de ventas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            producto TEXT NOT NULL,
            fecha TEXT NOT NULL,
            monto REAL NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    ''')
    
    

    conexion.commit()
    conexion.close()
    print("✔ Tablas creadas correctamente.")

def ver_clientes():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conexion.close()
    return clientes  # ✅ Importante: devolvemos la lista

# Para probar si ejecutás el archivo directamente
if __name__ == "__main__":
    crear_tablas()
    for c in ver_clientes():
        print(c)
