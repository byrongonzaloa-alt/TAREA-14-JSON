Restaurante App

Estudiante
Byron Abarca

Descripción del Proyecto
Restaurante App, desarrollada en Python con Programación Orientada a Objetos y Tkinter, gestiona la información de un restaurante con inicio de sesión, administración de usuarios y productos. En la Semana 14 se optimizó su interfaz gráfica usando contenedores para una mejor organización y experiencia de uso. El sistema permite registrar, consultar, actualizar y eliminar productos, manteniendo la arquitectura modular y el almacenamiento de datos en archivos JSON.

________________________________________
Objetivo

El propósito de este trabajo es diseñar y perfeccionar una herramienta de administración para un restaurante, basada en Programación Orientada a Objetos y elementos gráficos de Tkinter, conservando un diseño modular y guardando la información de forma permanente en archivos JSON.
________________________________________

Funcionalidades

La aplicación cuenta con las siguientes funcionalidades:
•	Inicio de sesión mediante usuario y contraseña.
•	Validación de usuarios.
•	Consulta de información de usuarios.
•	Visualización de productos.
•	Registro de nuevos productos.
•	Consulta o carga de productos mediante su código.
•	Actualización de información de productos.
•	Eliminación de productos.
•	Persistencia de los productos en el archivo productos.json.
•	Interfaz gráfica desarrollada con Tkinter.
•	Uso de componentes como botones, etiquetas, entradas y tablas.
•	Uso de contenedores para organizar la interfaz.
•	Separación entre la interfaz, modelos, servicios y datos.
________________________________________

Componentes y contenedores

En esta versión del proyecto se incorporan componentes y contenedores de Tkinter para mejorar la organización de la interfaz.
Entre los componentes utilizados se encuentran:
•	Label: permite mostrar títulos y textos informativos.
•	Entry: permite ingresar datos de usuarios y productos.
•	Button: permite ejecutar las diferentes operaciones.
•	Treeview: permite mostrar los productos de manera organizada.
•	Frame: permite dividir y organizar las diferentes áreas de la ventana.
•	LabelFrame: permite agrupar elementos relacionados.
•	messagebox: permite mostrar mensajes de información, advertencia o confirmación.
________________________________________

 Estructura del proyecto
 
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
│
└── README.md

Reflexión

Al desarrollar este proyecto, comprendí cómo la Programación Orientada a Objetos da estructura y claridad a una aplicación real. Me di cuenta de que una buena interfaz con Tkinter no es solo colocar elementos, sino organizarlos para que sean intuitivos. Aprendí también que guardar información en archivos JSON permite que los datos se conserven entre sesiones, y que separar la vista de la lógica hace que el código sea más limpio, fácil de corregir y listo para crecer.
