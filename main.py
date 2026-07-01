"""
=============================================================================
UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA (UNAD)
Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)
Programa: Ingeniería de Sistemas
Curso: Programación - Período 16-02 (2026)

FASE 4: COMPONENTE PRÁCTICO - PRÁCTICAS SIMULADAS
Proyecto: Sistema Integral de Gestión Software FJ

AUTORES:
1. Verónica Valencia Cortez
2. Jefferson Matabanchoy Lectamo

GRUPO COLABORATIVO:213023_36
TUTOR:Juan Manuel Gonzales Silva
FECHA DE ENTREGA:02/06/2026
=============================================================================
Descripción: Archivo de ejecución principal encargado de inicializar la 
             interfaz gráfica del sistema, garantizando el control de 
             excepciones y logs de eventos acordes a la guía de actividades.
=============================================================================
"""

import interfaz.ventana_principal


def main():
    """
    Función principal que inicia
    la ventana principal del sistema.
    """
    app = interfaz.ventana_principal.VentanaPrincipal()
    app.ejecutar()


if __name__ == "__main__":
    main()