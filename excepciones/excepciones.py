"""
Excepciones personalizadas del sistema
Software FJ
"""


class ClienteError(Exception):
    """Errores relacionados con clientes"""
    pass


class ServicioError(Exception):
    """Errores relacionados con servicios"""
    pass


class ReservaError(Exception):
    """Errores relacionados con reservas"""
    pass


class ValidacionError(Exception):
    """Errores de validación"""
    pass


class OperacionError(Exception):
    """Errores relacionados con operaciones"""
    pass