"""
Proyecto: Sistema Integral de Gestión
Software FJ

Integrante:
Verónica Valencia Cortez

Archivo principal del sistema.
Se encarga de iniciar la interfaz gráfica.
"""

import interfaz.ventana_principal


def main():
    """{}
    Función principal que inicia
    la ventana principal del sistema.
    """

    app = interfaz.ventana_principal.VentanaPrincipal()
    app.ejecutar()


if __name__ == "__main__":
    main()