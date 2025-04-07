from clientes import agregar_cliente, editar_cliente, eliminar_cliente
from clientes import ver_clientes
from cuentas import agregar_cuenta, ver_cuentas, ver_cuentas_cliente
from ventas import registrar_venta, ver_ventas, ver_ventas_cliente
from importar import importar_datos_csv

def menu_clientes():
    while True:
        print("\n📁 MENÚ CLIENTES")
        print("1. Ver clientes")
        print("2. Agregar cliente")
        print("3. Editar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            for c in ver_clientes():
                print(f"ID: {c[0]}, Nombre: {c[1]}, Email: {c[2]}, Teléfono: {c[3]}")
        elif opcion == "2":
            nombre = input("Nombre: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            agregar_cliente(nombre, email, telefono)
        elif opcion == "3":
            email = input("Email del cliente a editar: ")
            nuevo_nombre = input("Nuevo nombre (dejar vacío para mantener): ")
            nuevo_telefono = input("Nuevo teléfono (dejar vacío para mantener): ")
            editar_cliente(email, nuevo_nombre or None, nuevo_telefono or None)
        elif opcion == "4":
            email = input("Email del cliente a eliminar: ")
            eliminar_cliente(email)
        elif opcion == "5":
            break
        else:
            print("❌ Opción inválida.")

def menu_cuentas():
    while True:
        print("\n🏦 MENÚ CUENTAS")
        print("1. Ver todas las cuentas")
        print("2. Ver cuentas de un cliente")
        print("3. Agregar cuenta")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ver_cuentas()
        elif opcion == "2":
            email = input("Email del cliente: ")
            ver_cuentas_cliente(email)
        elif opcion == "3":
            email = input("Email del cliente: ")
            tipo = input("Tipo de cuenta (ej. Caja de ahorro): ")
            saldo = float(input("Saldo inicial: "))
            agregar_cuenta(email, tipo, saldo)
        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida.")

def menu_ventas():
    while True:
        print("\n💵 MENÚ VENTAS")
        print("1. Ver todas las ventas")
        print("2. Ver ventas por cliente")
        print("3. Registrar nueva venta")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ver_ventas()
        elif opcion == "2":
            email = input("Email del cliente: ")
            ver_ventas_cliente(email)
        elif opcion == "3":
            email = input("Email del cliente: ")
            producto = input("Producto: ")
            monto = float(input("Monto: "))
            fecha = input("Fecha (YYYY-MM-DD): ")
            registrar_venta(email, producto, monto, fecha)
        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida.")

def menu_importador():
    print("\n📥 IMPORTACIÓN DE DATOS CSV")
    importar_datos_csv()

def main():
    while True:
        print("\n🧩 MENÚ PRINCIPAL CRM")
        print("1. Clientes")
        print("2. Cuentas")
        print("3. Ventas")
        print("4. Importar desde CSV")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_cuentas()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            menu_importador()
        elif opcion == "5":
            print("👋 Cerrando CRM. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
