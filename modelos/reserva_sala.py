from modelos.servicio import Servicio


class ReservaSala(Servicio):
    """
    Servicio de reserva de salas.
    """

    def __init__(
        self,
        identificador,
        nombre,
        costo_base,
        capacidad
    ):

        super().__init__(
            identificador,
            nombre,
            costo_base
        )

        self.capacidad = capacidad

    def calcular_costo(
        self,
        horas=1,
        descuento=0,
        impuesto=0
    ):

        subtotal = self.costo_base * horas

        subtotal -= descuento

        total = subtotal + (
            subtotal * impuesto / 100
        )

        return total

    def describir(self):

        return (
            f"Reserva de sala para "
            f"{self.capacidad} personas."
        )

    def mostrar_info(self):

        return (
            f"Servicio: {self.nombre}\n"
            f"Costo Base: ${self.costo_base}\n"
            f"Capacidad: {self.capacidad}"
        )