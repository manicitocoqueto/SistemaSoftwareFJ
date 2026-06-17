from abc import ABC, abstractmethod
from datetime import datetime


class Entidad(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.
    """

    def __init__(self, identificador):
        self._id = identificador
        self._fecha_creacion = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @abstractmethod
    def mostrar_info(self):
        pass