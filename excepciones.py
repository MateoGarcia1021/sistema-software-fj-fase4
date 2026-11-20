# excepciones.py
# Excepciones personalizadas para el sistema de Software FJ.


class DatoInvalidoError(Exception):
    """Error cuando un dato no cumple con lo esperado."""
    pass


class ServicioNoDisponibleError(Exception):
    """Error cuando un servicio no esta disponible."""
    pass


class OperacionReservaError(Exception):
    """Error al confirmar, cancelar o procesar una reserva."""
    pass
