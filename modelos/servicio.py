from abc import ABC, abstractmethod

from modelos.entidad import Entidad
from excepciones.excepciones import ServicioError


class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa un servicio general.
    """

    def __init__(self, identificador, nombre, costo_base):

        super().__init__(identificador)

        if costo_base <= 0:
            raise ServicioError(
                "El costo del servicio debe ser mayor que cero."
            )

        self._nombre = nombre
        self._costo_base = costo_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_base(self):
        return self._costo_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir(self):
        pass

    def mostrar_info(self):
        return (
            f"Servicio: {self._nombre}\n"
            f"Costo Base: ${self._costo_base}"
        )