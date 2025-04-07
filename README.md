# 🧾 CRM de Clientes en Python

Este es un proyecto de CRM (Customer Relationship Management) desarrollado en **Python**, que permite gestionar **clientes**, **cuentas bancarias** y **ventas**. Utiliza **SQLite** como base de datos y permite importar datos desde archivos **CSV** fácilmente.

---

## 📁 Estructura del Proyecto

crm_negocio/ 
│ ├── data/ # Archivos de datos 
│ ├── clientes.csv 
│ ├── cuentas.csv 
│ ├── ventas.csv 
│ └── crm.db 
│ ├── clientes.py # Gestión de clientes 
├── cuentas.py # Gestión de cuentas 
├── ventas.py # Gestión de ventas 
├── importar.py # Importación de datos CSV 
├── db.py # Base de datos y creación de tablas 
├── main.py # Menú principal del sistema 
├── README.md # Documentación del proyecto 
└── LICENSE # Licencia del proyecto


---

## ⚙️ Funcionalidades

- 👤 Gestión de clientes (agregar, editar, eliminar, listar)
- 💳 Gestión de cuentas (vinculadas a clientes)
- 🛒 Gestión de ventas (vinculadas a clientes)
- 📥 Importación de datos desde archivos CSV
- 📊 Visualización de datos en consola
- 🧪 Persistencia con base de datos SQLite (local)

---

## 🚀 Cómo usar

### 1. Clonar el repositorio


git clone https://github.com/AluheMaeda/crm-python.git
cd crm-python/crm_negocio

### 2. Crear las tablas
Ejecutá el archivo db.py para generar las tablas necesarias:

python db.py

### 3. Importar datos desde CSV
Ejecutá el sistema:

python main.py

Elegí la opción para importar los datos. Los archivos CSV deben estar en la carpeta data/.

---

📂 Formato de los archivos CSV

clientes.py :
Nombre,Email,Teléfono
Juan Gómez,juan@mail.com,1122334455

cuentas.py :
Cliente,Tipo,Saldo
Juan Gómez,Caja de ahorro,50000

ventas.py :
Cliente,Producto,Monto,Fecha
Juan Gómez,Notebook,450000,2025-04-01

---


🛠 Requisitos
Python 3.8 o superior

No se requieren librerías externas

---

👤 Autor
Desarrollado por Aluhe Maeda – @AluheMaeda

---

📄 Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más información.