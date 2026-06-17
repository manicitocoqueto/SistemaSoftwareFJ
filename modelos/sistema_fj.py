from logs.config_log import registrar_info


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

        self.clientes.append(cliente)

        registrar_info(
            f"Cliente agregado: {cliente.nombre}"
        )

    def agregar_servicio(self, servicio):

        self.servicios.append(servicio)

        registrar_info(
            f"Servicio agregado: {servicio.nombre}"
        )

    def agregar_reserva(self, reserva):

        self.reservas.append(reserva)

        registrar_info(
            "Reserva agregada correctamente."
        )

    def listar_clientes(self):

        return self.clientes

    def listar_servicios(self):

        return self.servicios

    def listar_reservas(self):

        return self.reservas