from modelos.entidad import Entidad
from excepciones.excepciones import ValidacionError
from logs.config_log import registrar_info, registrar_error


class Cliente(Entidad):
    """
    Clase que representa un cliente del sistema.
    """

    def __init__(self, identificador, nombre, documento, correo, telefono):

        super().__init__(identificador)

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):

        if not self.__nombre.strip():

            registrar_error(
                "Nombre de cliente vacío."
            )

            raise ValidacionError(
                "El nombre no puede estar vacío."
            )

        if not self.__documento.isdigit():

            registrar_error(
                f"Documento inválido: {self.__documento}"
            )

            raise ValidacionError(
                "El documento debe contener solo números."
            )

        if "@" not in self.__correo:

            registrar_error(
                f"Correo inválido: {self.__correo}"
            )

            raise ValidacionError(
                "Correo electrónico inválido."
            )

        if not self.__telefono.isdigit():

            registrar_error(
                f"Teléfono inválido: {self.__telefono}"
            )

            raise ValidacionError(
                "El teléfono debe contener solo números."
            )

        registrar_info(
            f"Cliente registrado correctamente: {self.__nombre}"
        )

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_info(self):

        return (
            f"ID: {self.id}\n"
            f"Nombre: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )