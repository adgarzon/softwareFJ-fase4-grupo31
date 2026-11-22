# exceptions/excepciones.py
# Jerarquía de excepciones personalizadas del sistema Software FJ.


class SoftwareFJError(Exception):
    """Excepción base: todas las excepciones del sistema heredan de ella."""


class ClienteInvalidoError(SoftwareFJError):
    """Datos de cliente incorrectos o incompletos."""


class ServicioInvalidoError(SoftwareFJError):
    """Parámetros de un servicio incorrectos."""


class ServicioNoDisponibleError(SoftwareFJError):
    """Se intenta reservar un servicio que no está disponible."""


class ReservaInvalidaError(SoftwareFJError):
    """La reserva no cumple las reglas del negocio."""


class OperacionNoPermitidaError(SoftwareFJError):
    """Cambio de estado no permitido (por ejemplo, cancelar una reserva procesada)."""


class CalculoInconsistenteError(SoftwareFJError):
    """El cálculo del costo produjo un valor imposible."""
