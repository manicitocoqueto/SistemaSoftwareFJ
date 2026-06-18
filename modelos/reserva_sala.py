from modelos.servicio import Servicio
from excepciones.excepciones import ServicioError


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

        if capacidad <= 0:

            raise ServicioError(
                "La capacidad debe ser mayor que cero."
            )

        self.capacidad = capacidad

    def calcular_costo(
        self,
        horas=1,
        descuento=0,
        impuesto=0
    ):

        if horas <= 0:

            raise ServicioError(
                "Las horas deben ser mayores que cero."
            )

        if descuento < 0:

            raise ServicioError(
                "El descuento no puede ser negativo."
            )

        if impuesto < 0:

            raise ServicioError(
                "El impuesto no puede ser negativo."
            )

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