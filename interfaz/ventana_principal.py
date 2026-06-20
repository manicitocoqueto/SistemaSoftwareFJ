import tkinter as tk
from tkinter import messagebox


class VentanaPrincipal:
    """
    Interfaz gráfica principal del Sistema
    Integral de Gestión Software FJ.
    """

    def __init__(self):
        """
        Inicializa la ventana principal y
        sus componentes gráficos.
        """

        self.ventana = tk.Tk()

        self.ventana.title("Sistema Integral Software FJ")
        self.ventana.geometry("700x500")
        self.ventana.resizable(False, False)

        titulo = tk.Label(
            self.ventana,
            text="Sistema Integral de Gestión Software FJ",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=20)

        boton_cliente = tk.Button(
            self.ventana,
            text="Registrar Cliente",
            width=25,
            command=self.registrar_cliente
        )
        boton_cliente.pack(pady=10)

        boton_servicio = tk.Button(
            self.ventana,
            text="Crear Servicio",
            width=25,
            command=self.crear_servicio
        )
        boton_servicio.pack(pady=10)

        boton_reserva = tk.Button(
            self.ventana,
            text="Crear Reserva",
            width=25,
            command=self.crear_reserva
        )
        boton_reserva.pack(pady=10)

        boton_salir = tk.Button(
            self.ventana,
            text="Salir",
            width=25,
            command=self.ventana.destroy
        )
        boton_salir.pack(pady=20)

    def registrar_cliente(self):
        messagebox.showinfo(
            "Cliente",
            "Módulo de clientes en construcción."
        )

    def crear_servicio(self):
        messagebox.showinfo(
            "Servicio",
            "Módulo de servicios en construcción."
        )

    def crear_reserva(self):
        messagebox.showinfo(
            "Reserva",
            "Módulo de reservas en construcción."
        )

    def ejecutar(self):
        self.ventana.mainloop()