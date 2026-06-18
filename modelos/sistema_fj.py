from logs.config_log import (
    registrar_info,
    registrar_error
)

from excepciones.excepciones import (
    ValidacionError,
    OperacionError
)


class SistemaFJ:
    """
    Clase que administra clientes,
    servicios y reservas.
    """

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):

        try:

            for c in self.clientes:

                if c.documento == cliente.documento:

                    raise ValidacionError(
                        "Ya existe un cliente con ese documento."
                    )

        except ValidacionError as error:

            registrar_error(str(error))
            raise

        else:

            self.clientes.append(cliente)

            registrar_info(
                f"Cliente agregado: {cliente.nombre}"
            )

    def agregar_servicio(self, servicio):

        try:

            for s in self.servicios:

                if s.nombre == servicio.nombre:

                    raise ValidacionError(
                        "Ya existe un servicio con ese nombre."
                    )

        except ValidacionError as error:

            registrar_error(str(error))
            raise

        else:

            self.servicios.append(servicio)

            registrar_info(
                f"Servicio agregado: {servicio.nombre}"
            )

    def agregar_reserva(self, reserva):

        try:

            if reserva is None:

                raise OperacionError(
                    "La reserva no puede ser nula."
                )

        except OperacionError as error:

            registrar_error(str(error))
            raise

        else:

            self.reservas.append(reserva)

            registrar_info(
                "Reserva agregada correctamente."
            )

        finally:

            registrar_info(
                "Proceso de registro de reserva finalizado."
            )

    def listar_clientes(self):

        return self.clientes

    def listar_servicios(self):

        return self.servicios

    def listar_reservas(self):

        return self.reservas