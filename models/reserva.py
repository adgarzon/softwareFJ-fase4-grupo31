# models/reserva.py
# Reserva: integra cliente, servicio, duración y estado.
from models.entidad import Entidad
from models.cliente import Cliente
from models.servicio import Servicio
from exceptions.excepciones import (
    ReservaInvalidaError, ServicioNoDisponibleError,
    OperacionNoPermitidaError, ServicioInvalidoError,
)
from utils.logger import obtener_logger

log = obtener_logger()


class Reserva(Entidad):
    PENDIENTE, CONFIRMADA, CANCELADA, PROCESADA = (
        "PENDIENTE", "CONFIRMADA", "CANCELADA", "PROCESADA")

    def __init__(self, cliente, servicio, duracion):
        super().__init__()
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("La reserva requiere un objeto Cliente.")
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("La reserva requiere un objeto Servicio.")
        if not servicio.disponible:
            raise ServicioNoDisponibleError(f"'{servicio.nombre}' no está disponible.")
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = Reserva.PENDIENTE
        self._total = None

    @property
    def estado(self):
        return self._estado

    def confirmar(self):
        if self._estado != Reserva.PENDIENTE:
            raise OperacionNoPermitidaError(
                f"Solo se confirma una reserva PENDIENTE (estado actual: {self._estado}).")
        self._estado = Reserva.CONFIRMADA
        log.info("Reserva #%s confirmada", self.id)

    def cancelar(self):
        if self._estado == Reserva.PROCESADA:
            raise OperacionNoPermitidaError("No se puede cancelar una reserva ya procesada.")
        self._estado = Reserva.CANCELADA
        log.info("Reserva #%s cancelada", self.id)

    def procesar(self, impuesto=0.19, descuento=0.0):
        """Calcula el total. Usa try/except/else/finally y encadenamiento."""
        if self._estado != Reserva.CONFIRMADA:
            raise OperacionNoPermitidaError("Solo se procesan reservas CONFIRMADAS.")
        try:
            total = self._servicio.calcular_costo(self._duracion, impuesto, descuento)
        except ServicioInvalidoError as error:
            # Encadenamiento: la nueva excepción conserva la causa original.
            raise ReservaInvalidaError(
                f"No se pudo procesar la reserva #{self.id}") from error
        else:
            # Solo se ejecuta si NO hubo excepción.
            self._total = total
            self._estado = Reserva.PROCESADA
            log.info("Reserva #%s procesada. Total: %.2f", self.id, total)
            return total
        finally:
            # Se ejecuta siempre, haya o no error.
            log.info("Fin del intento de procesamiento de la reserva #%s", self.id)

    def describir(self):
        total = f"${self._total:,.2f}" if self._total is not None else "sin calcular"
        return (f"Reserva #{self.id}: {self._cliente.nombre} -> {self._servicio.nombre} "
                f"x{self._duracion} [{self._estado}] {total}")
