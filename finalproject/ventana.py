import tkinter as tk
from tkinter import ttk
import markdown

class InterfazPresentacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Software de Algoritmos de IA")

        # Configuración del tamaño de la ventana
        self.ventana.geometry("800x500")  # Aumentamos el tamaño de la ventana

        # Cambiamos el fondo de la ventana principal
        self.ventana.configure(bg="#4CAF50")  # Color de fondo verde

        # Cargar texto desde un archivo .txt
        with open("finalproject/overview_problem.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        # Etiqueta de presentación con fondo colorido y texto cargado desde el archivo
        label_presentacion = tk.Label(
            ventana,
            text=contenido,
            font=("Arial", 14),  # Disminuir el tamaño de la fuente para ajustarse mejor
            pady=20,
            wraplength=700,  # Ajustar la longitud de envoltura según sea necesario
            justify="center",  # Ajustar la justificación del texto
            bg="#4CAF50",  # Color de fondo verde
            fg="white",  # Texto en color blanco
        )
        label_presentacion.pack()

        # Estilo para los botones con colores personalizados
        estilo_botones = ttk.Style()
        estilo_botones.configure(
            "TButton",
            font=("Arial", 18),
            foreground="#ffffff",  # Texto en color blanco
            background="#2196F3",  # Color de fondo azul
        )

        # Botón para el Administrador
        btn_administrador = ttk.Button(
            ventana, text="Administrador", command=self.ventana_administrador
        )
        btn_administrador.pack(pady=20)

        # Botón para el Usuario
        btn_usuario = ttk.Button(ventana, text="Usuario", command=self.ventana_usuario)
        btn_usuario.pack(pady=20)

    def ventana_administrador(self):
        # Ocultar la ventana principal
        self.ventana.withdraw()

        # Crear ventana para el Administrador
        ventana_admin = tk.Toplevel(self.ventana)
        ventana_admin.title("Bienvenido Administrador")

        # Cambiar fondo de la ventana del Administrador
        ventana_admin.configure(bg="#FF9800")  # Color de fondo naranja

        tk.Label(
            ventana_admin,
            text="¡Bienvenido Administrador!",
            font=("Arial", 20),
            pady=20,
            bg="#FF9800",  # Color de fondo naranja
            fg="white",  # Texto en color blanco
        ).pack()

        # Botón para regresar a la ventana principal
        btn_regresar = ttk.Button(
            ventana_admin, text="Regresar", command=lambda: self.regresar_ventana_principal(ventana_admin)
        )
        btn_regresar.pack(pady=20)

    def ventana_usuario(self):
        # Ocultar la ventana principal
        self.ventana.withdraw()

        # Crear ventana para el Usuario
        ventana_usuario = tk.Toplevel(self.ventana)
        ventana_usuario.title("Bienvenido Usuario")

        # Cambiar fondo de la ventana del Usuario
        ventana_usuario.configure(bg="#E91E63")  # Color de fondo rosa

        tk.Label(
            ventana_usuario,
            text="¡Bienvenido Usuario!",
            font=("Arial", 20),
            pady=20,
            bg="#E91E63",  # Color de fondo rosa
            fg="white",  # Texto en color blanco
        ).pack()

        # Botón para regresar a la ventana principal
        btn_regresar = ttk.Button(
            ventana_usuario, text="Regresar", command=lambda: self.regresar_ventana_principal(ventana_usuario)
        )
        btn_regresar.pack(pady=20)

    def regresar_ventana_principal(self, ventana_secundaria):
        # Destruir la ventana secundaria actual
        ventana_secundaria.destroy()

        # Mostrar la ventana principal nuevamente
        self.ventana.deiconify()

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = InterfazPresentacion(ventana_principal)
    ventana_principal.mainloop()
