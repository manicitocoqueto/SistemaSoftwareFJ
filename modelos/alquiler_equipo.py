from modelos.servicio import Servicio
from excepciones.excepciones import ServicioError


class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos.
    """

    def __init__(
        self,
        identificador,
        nombre,
        costo_base,
        tipo_equipo
    ):

        super().__init__(
            identificador,
            nombre,
            costo_base
        )

        if not tipo_equipo.strip():

            raise ServicioError(
                "El tipo de equipo no puede estar vacío."
            )

        self.tipo_equipo = tipo_equipo

    def calcular_costo(
        self,
        dias=1,
        descuento=0,
        impuesto=0
    ):

        if dias <= 0:

            raise ServicioError(
                "Los días deben ser mayores que cero."
            )

        if descuento < 0:

            raise ServicioError(
                "El descuento no puede ser negativo."
            )

        if impuesto < 0:

            raise ServicioError(
                "El impuesto no puede ser negativo."
            )

        subtotal = self.costo_base * dias

        subtotal -= descuento

        total = subtotal + (
            subtotal * impuesto / 100
        )

        return total

    def describir(self):

        return (
            f"Alquiler de equipo tipo "
            f"{self.tipo_equipo}"
        )

    def mostrar_info(self):

        return (
            f"Servicio: {self.nombre}\n"
            f"Costo Base: ${self.costo_base}\n"
            f"Equipo: {self.tipo_equipo}"
        )