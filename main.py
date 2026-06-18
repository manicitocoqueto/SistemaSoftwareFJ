"""
Proyecto: Sistema Integral de Gestión
Software FJ

Integrante:
Veronica Valencia Cortez

Archivo principal del sistema.
Se encarga de iniciar la interfaz gráfica.
"""

from interfaz.ventana_principal import VentanaPrincipal


def main():
    """
    Función principal que inicia
    la ventana principal del sistema.
    """

    app = VentanaPrincipal()
    app.ejecutar()


if __name__ == "__main__":
    main()