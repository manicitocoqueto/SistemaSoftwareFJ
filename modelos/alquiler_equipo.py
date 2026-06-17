from modelos.servicio import Servicio


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

        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias=1):
        return self.costo_base * dias

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