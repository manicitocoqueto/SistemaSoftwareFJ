from modelos.servicio import Servicio


class Asesoria(Servicio):
    """
    Servicio de asesoría especializada.
    """

    def __init__(
        self,
        identificador,
        nombre,
        costo_base,
        especialidad
    ):

        super().__init__(
            identificador,
            nombre,
            costo_base
        )

        self.especialidad = especialidad

    def calcular_costo(self, horas=1):
        return self.costo_base * horas

    def describir(self):
        return (
            f"Asesoría especializada en "
            f"{self.especialidad}"
        )

    def mostrar_info(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Costo Base: ${self.costo_base}\n"
            f"Especialidad: {self.especialidad}"
        )