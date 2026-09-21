import tkinter as tk
from tkinter import messagebox, ttk


class MainView(tk.Frame):
    def __init__(
        self,
        master,
        restaurante_servicio,
        usuario_actual,
        al_cerrar_sesion
    ):
        super().__init__(master, bg="#f7fafc")

        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion

        self.contenido = None
        self.etiqueta_estado = None
        self.botones_menu = {}

        self.producto_codigo_entry = None
        self.producto_nombre_entry = None
        self.producto_precio_entry = None
        self.producto_categoria_entry = None
        self.producto_stock_entry = None

        self.tabla_productos = None
        self.tabla_usuarios = None

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        self.color_fondo = "#f7fafc"
        self.color_panel = "#ffffff"
        self.color_encabezado = "#1f2a44"
        self.color_texto = "#243447"
        self.color_secundario = "#dbeafe"
        self.color_resaltado = "#2563eb"

        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "MenuApp.TButton",
            background="#334155",
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(12, 10),
            borderwidth=0,
            anchor="w",
        )

        estilo.map(
            "MenuApp.TButton",
            background=[("active", "#475569")]
        )

        estilo.configure(
            "MenuActivo.TButton",
            background=self.color_resaltado,
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(12, 10),
            borderwidth=0,
            anchor="w",
        )

        estilo.configure(
            "Secundario.TButton",
            background="#1f2a44",
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(10, 7),
            borderwidth=0,
        )

        estilo.configure(
            "Accion.TButton",
            background=self.color_resaltado,
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(10, 7),
            borderwidth=0,
        )

        estilo.configure(
            "Eliminar.TButton",
            background="#e11d48",
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(10, 7),
            borderwidth=0,
        )

        estilo.configure(
            "Treeview.Heading",
            background=self.color_secundario,
            foreground=self.color_encabezado,
            font=("Arial", 10, "bold"),
        )

    def construir_interfaz(self):
        frame_sidebar = tk.Frame(
            self,
            bg=self.color_encabezado,
            width=190,
            padx=16,
            pady=18
        )

        frame_sidebar.pack(
            side="left",
            fill="y"
        )

        frame_sidebar.pack_propagate(False)

        tk.Label(
            frame_sidebar,
            text="RESTAURANTE",
            bg=self.color_encabezado,
            fg="#ffffff",
            font=("Arial", 16, "bold"),
        ).pack(
            anchor="w",
            pady=(0, 8)
        )

        tk.Label(
            frame_sidebar,
            text=self.usuario_actual.nombre,
            bg=self.color_encabezado,
            fg="#dbeafe",
            font=("Arial", 10),
            wraplength=150,
            justify="left",
        ).pack(
            anchor="w",
            pady=(0, 24)
        )

        self.crear_boton_menu(
            frame_sidebar,
            "Inicio",
            self.mostrar_inicio
        )

        self.crear_boton_menu(
            frame_sidebar,
            "Usuarios",
            self.mostrar_usuarios
        )

        self.crear_boton_menu(
            frame_sidebar,
            "Productos",
            self.mostrar_productos
        )

        tk.Frame(
            frame_sidebar,
            bg=self.color_encabezado
        ).pack(
            fill="both",
            expand=True
        )

        ttk.Button(
            frame_sidebar,
            text="Cerrar sesion",
            command=self.cerrar_sesion,
            style="Eliminar.TButton"
        ).pack(
            fill="x",
            pady=(16, 0)
        )

        frame_principal = tk.Frame(
            self,
            bg=self.color_fondo
        )

        frame_principal.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.contenido = tk.Frame(
            frame_principal,
            bg=self.color_fondo,
            padx=28,
            pady=24
        )

        self.contenido.pack(
            fill="both",
            expand=True
        )

        barra_estado = tk.Frame(
            frame_principal,
            bg=self.color_secundario,
            padx=18,
            pady=8
        )

        barra_estado.pack(
            fill="x",
            side="bottom"
        )

        self.etiqueta_estado = tk.Label(
            barra_estado,
            bg=self.color_secundario,
            fg=self.color_texto,
            font=("Arial", 10),
        )

        self.etiqueta_estado.pack(
            side="left"
        )

        self.mostrar_inicio()

    def crear_boton_menu(
        self,
        contenedor,
        texto,
        comando
    ):
        boton = ttk.Button(
            contenedor,
            text=texto,
            command=comando,
            style="MenuApp.TButton"
        )

        boton.pack(
            fill="x",
            pady=(0, 8)
        )

        self.botones_menu[texto] = boton

    def marcar_seccion(self, seccion):
        for texto, boton in self.botones_menu.items():

            if texto == seccion:
                boton.configure(
                    style="MenuActivo.TButton"
                )
            else:
                boton.configure(
                    style="MenuApp.TButton"
                )

    def limpiar_contenido(self):
        assert self.contenido is not None

        for widget in self.contenido.winfo_children():
            widget.destroy()

    def actualizar_barra_estado(self):
        assert self.etiqueta_estado is not None

        self.etiqueta_estado.config(
            text=(
                f"Productos: "
                f"{self.restaurante_servicio.cantidad_productos()} | "
                f"Usuarios: "
                f"{self.restaurante_servicio.cantidad_usuarios()} | "
                "Datos JSON locales"
            )
        )

    def mostrar_inicio(self):
        self.marcar_seccion("Inicio")
        self.limpiar_contenido()
        self.actualizar_barra_estado()

        assert self.contenido is not None

        tk.Label(
            self.contenido,
            text="Panel principal",
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 20, "bold"),
        ).pack(
            anchor="w",
            pady=(0, 8)
        )

        tk.Label(
            self.contenido,
            text=(
                "Consulte usuarios y gestione "
                "productos desde el menu lateral."
            ),
            bg=self.color_fondo,
            fg=self.color_texto,
            font=("Arial", 12),
        ).pack(
            anchor="w",
            pady=(0, 22)
        )

        resumen = tk.Frame(
            self.contenido,
            bg=self.color_fondo
        )

        resumen.pack(
            fill="x"
        )

        self.crear_tarjeta_resumen(
            resumen,
            "Usuarios registrados",
            self.restaurante_servicio.cantidad_usuarios()
        )

        self.crear_tarjeta_resumen(
            resumen,
            "Productos registrados",
            self.restaurante_servicio.cantidad_productos()
        )

    def crear_tarjeta_resumen(
        self,
        contenedor,
        titulo,
        valor
    ):
        tarjeta = tk.Frame(
            contenedor,
            bg=self.color_panel,
            padx=18,
            pady=16
        )

        tarjeta.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 14)
        )

        tk.Label(
            tarjeta,
            text=titulo,
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")

        tk.Label(
            tarjeta,
            text=str(valor),
            bg=self.color_panel,
            fg=self.color_resaltado,
            font=("Arial", 24, "bold"),
        ).pack(
            anchor="w",
            pady=(8, 0)
        )

    def mostrar_usuarios(self):
        self.marcar_seccion("Usuarios")
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_titulo_seccion(
            "Usuarios registrados"
        )

        listado = self.crear_listado(
            self.contenido,
            "Consulta de usuarios"
        )

        self.tabla_usuarios = self.crear_tabla(
            listado,
            (
                "identificacion",
                "nombre",
                "usuario"
            ),
            (
                "Identificacion",
                "Nombre",
                "Usuario"
            )
        )

        self.refrescar_usuarios()

    def refrescar_usuarios(self):
        assert self.tabla_usuarios is not None

        self.limpiar_tabla(
            self.tabla_usuarios
        )

        for usuario in self.restaurante_servicio.listar_usuarios():
            self.tabla_usuarios.insert(
                "",
                tk.END,
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario
                )
            )

        self.actualizar_barra_estado()

    def mostrar_productos(self):
        self.marcar_seccion("Productos")
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_titulo_seccion(
            "Gestion de productos"
        )

        formulario = tk.LabelFrame(
            self.contenido,
            text="Datos del producto",
            bg=self.color_panel,
            fg=self.color_encabezado,
            font=("Arial", 10, "bold"),
            padx=14,
            pady=14
        )

        formulario.pack(
            fill="x",
            pady=(0, 16)
        )

        self.producto_codigo_entry = self.crear_campo(
            formulario,
            "Codigo",
            0
        )

        self.producto_nombre_entry = self.crear_campo(
            formulario,
            "Nombre",
            1
        )

        self.producto_precio_entry = self.crear_campo(
            formulario,
            "Precio",
            2
        )

        self.producto_categoria_entry = self.crear_campo(
            formulario,
            "Categoria",
            3
        )

        self.producto_stock_entry = self.crear_campo(
            formulario,
            "Stock",
            4
        )

        acciones = tk.Frame(
            formulario,
            bg=self.color_panel
        )

        acciones.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=(12, 0)
        )

        ttk.Button(
            acciones,
            text="Registrar",
            command=self.registrar_producto,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            acciones,
            text="Cargar por codigo",
            command=self.cargar_producto,
            style="Secundario.TButton"
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            acciones,
            text="Actualizar",
            command=self.actualizar_producto,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            acciones,
            text="Eliminar",
            command=self.eliminar_producto,
            style="Eliminar.TButton"
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            acciones,
            text="Limpiar",
            command=self.limpiar_formulario_producto,
            style="Secundario.TButton"
        ).pack(
            side="left",
            padx=3
        )

        listado = self.crear_listado(
            self.contenido,
            "Productos registrados"
        )

        self.tabla_productos = self.crear_tabla(
            listado,
            (
                "codigo",
                "nombre",
                "precio",
                "categoria",
                "stock"
            ),
            (
                "Codigo",
                "Nombre",
                "Precio",
                "Categoria",
                "Stock"
            )
        )

        self.refrescar_productos()

    def crear_campo(
        self,
        contenedor,
        etiqueta,
        fila
    ):
        tk.Label(
            contenedor,
            text=etiqueta,
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 10, "bold")
        ).grid(
            row=fila,
            column=0,
            sticky="w",
            pady=(0, 8),
            padx=(0, 10)
        )

        entrada = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 10)
        )

        entrada.grid(
            row=fila,
            column=1,
            sticky="ew",
            pady=(0, 8)
        )

        return entrada

    def refrescar_productos(self):
        assert self.tabla_productos is not None

        self.limpiar_tabla(
            self.tabla_productos
        )

        for producto in self.restaurante_servicio.listar_productos():
            self.tabla_productos.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.categoria,
                    producto.stock
                )
            )

        self.actualizar_barra_estado()

    def obtener_datos_producto(self):
        assert self.producto_codigo_entry is not None
        assert self.producto_nombre_entry is not None
        assert self.producto_precio_entry is not None
        assert self.producto_categoria_entry is not None
        assert self.producto_stock_entry is not None

        return (
            self.producto_codigo_entry.get(),
            self.producto_nombre_entry.get(),
            self.producto_precio_entry.get(),
            self.producto_categoria_entry.get(),
            self.producto_stock_entry.get()
        )

    def registrar_producto(self):
        try:
            self.restaurante_servicio.registrar_producto(
                *self.obtener_datos_producto()
            )

            self.limpiar_formulario_producto()
            self.refrescar_productos()

            messagebox.showinfo(
                "Productos",
                "Producto registrado correctamente."
            )

        except ValueError as error:
            messagebox.showerror(
                "Productos",
                str(error)
            )

    def cargar_producto(self):
        assert self.producto_codigo_entry is not None

        codigo = (
            self.producto_codigo_entry
            .get()
            .strip()
        )

        producto = (
            self.restaurante_servicio
            .buscar_producto_por_codigo(codigo)
        )

        if producto is None:
            messagebox.showerror(
                "Productos",
                "No existe un producto con ese codigo."
            )
            return

        assert self.producto_nombre_entry is not None
        assert self.producto_precio_entry is not None
        assert self.producto_categoria_entry is not None
        assert self.producto_stock_entry is not None

        self.producto_nombre_entry.delete(
            0,
            tk.END
        )

        self.producto_nombre_entry.insert(
            0,
            producto.nombre
        )

        self.producto_precio_entry.delete(
            0,
            tk.END
        )

        self.producto_precio_entry.insert(
            0,
            producto.precio
        )

        self.producto_categoria_entry.delete(
            0,
            tk.END
        )

        self.producto_categoria_entry.insert(
            0,
            producto.categoria
        )

        self.producto_stock_entry.delete(
            0,
            tk.END
        )

        self.producto_stock_entry.insert(
            0,
            producto.stock
        )

    def actualizar_producto(self):
        try:
            self.restaurante_servicio.actualizar_producto(
                *self.obtener_datos_producto()
            )

            self.refrescar_productos()

            messagebox.showinfo(
                "Productos",
                "Producto actualizado correctamente."
            )

        except ValueError as error:
            messagebox.showerror(
                "Productos",
                str(error)
            )

    def eliminar_producto(self):
        assert self.producto_codigo_entry is not None

        codigo = (
            self.producto_codigo_entry
            .get()
            .strip()
        )

        try:
            self.restaurante_servicio.eliminar_producto(
                codigo
            )

            self.limpiar_formulario_producto()
            self.refrescar_productos()

            messagebox.showinfo(
                "Productos",
                "Producto eliminado correctamente."
            )

        except ValueError as error:
            messagebox.showerror(
                "Productos",
                str(error)
            )

    def limpiar_formulario_producto(self):
        for entrada in (
            self.producto_codigo_entry,
            self.producto_nombre_entry,
            self.producto_precio_entry,
            self.producto_categoria_entry,
            self.producto_stock_entry
        ):
            if entrada is not None:
                entrada.delete(
                    0,
                    tk.END
                )

    def crear_titulo_seccion(self, texto):
        assert self.contenido is not None

        tk.Label(
            self.contenido,
            text=texto,
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            pady=(0, 16)
        )

    def crear_listado(
        self,
        contenedor,
        titulo
    ):
        listado = tk.LabelFrame(
            contenedor,
            text=titulo,
            bg=self.color_panel,
            fg=self.color_encabezado,
            font=("Arial", 10, "bold"),
            padx=12,
            pady=12
        )

        listado.pack(
            fill="both",
            expand=True
        )

        return listado

    def crear_tabla(
        self,
        contenedor,
        columnas,
        encabezados
    ):
        frame_tabla = tk.Frame(
            contenedor,
            bg=self.color_panel
        )

        frame_tabla.pack(
            fill="both",
            expand=True
        )

        tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=12
        )

        barra = ttk.Scrollbar(
            frame_tabla,
            orient="vertical",
            command=tabla.yview
        )

        tabla.configure(
            yscrollcommand=barra.set
        )

        for columna, encabezado in zip(
            columnas,
            encabezados
        ):
            tabla.heading(
                columna,
                text=encabezado
            )

            tabla.column(
                columna,
                width=130,
                anchor="w"
            )

        tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        barra.pack(
            side="right",
            fill="y"
        )

        return tabla

    def limpiar_tabla(self, tabla):
        for item in tabla.get_children():
            tabla.delete(item)

    def cerrar_sesion(self):
        self.al_cerrar_sesion()