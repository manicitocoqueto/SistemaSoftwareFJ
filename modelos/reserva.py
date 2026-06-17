from excepciones.excepciones import (
    ReservaError,
    OperacionError
)


class Reserva:
    """
    Clase que representa una reserva de un servicio.
    """

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError(
                "La duración debe ser mayor que cero."
            )

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):
        """
        Confirma la reserva.
        """

        if self.__estado == "Cancelada":
            raise OperacionError(
                "No se puede confirmar una reserva cancelada."
            )

        self.__estado = "Confirmada"

    def cancelar(self):
        """
        Cancela la reserva.
        """

        if self.__estado == "Cancelada":
            raise OperacionError(
                "La reserva ya fue cancelada."
            )

        self.__estado = "Cancelada"

    def procesar(self):
        """
        Procesa la reserva y calcula el costo.
        """

        try:

            costo = self.__servicio.calcular_costo(
                self.__duracion
            )

        except Exception as error:

            raise ReservaError(
                "Error al procesar la reserva."
            ) from error

        else:

            return costo

        finally:

            print("Proceso de reserva finalizado.")

    def mostrar_info(self):
        """
        Muestra la información de la reserva.
        """

        return (
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}"
        )