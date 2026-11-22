# models/servicio.py
# Clase abstracta Servicio: define el contrato común de todos los servicios.
from abc import abstractmethod
from models.entidad import Entidad
from exceptions.excepciones import ServicioInvalidoError, CalculoInconsistenteError


class Servicio(Entidad):
    def __init__(self, nombre, tarifa_base, disponible=True):
        super().__init__()
        if not nombre or not isinstance(nombre, str):
            raise ServicioInvalidoError("El servicio necesita un nombre.")
        if not isinstance(tarifa_base, (int, float)) or tarifa_base <= 0:
            raise ServicioInvalidoError("La tarifa base debe ser un número mayor que cero.")
        self._nombre = nombre
        self._tarifa_base = float(tarifa_base)
        self._disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, estado):
        self._disponible = bool(estado)

    # Métodos abstractos que cada servicio especializado sobrescribe.
    @abstractmethod
    def costo_base(self, cantidad):
        """Costo sin impuestos ni descuentos."""

    @abstractmethod
    def validar_parametros(self, cantidad):
        """Lanza ServicioInvalidoError si la cantidad no es válida."""

    # "Sobrecarga" al estilo Python: un solo método con parámetros opcionales.
    # calcular_costo(c)                       -> costo base
    # calcular_costo(c, impuesto=0.19)        -> con IVA
    # calcular_costo(c, descuento=0.10)       -> con descuento
    # calcular_costo(c, impuesto=.19, descuento=.1) -> ambos
    def calcular_costo(self, cantidad, impuesto=0.0, descuento=0.0):
        self.validar_parametros(cantidad)
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise ServicioInvalidoError("Impuesto y descuento deben estar entre 0 y 1.")
        subtotal = self.costo_base(cantidad) * (1 - descuento)
        total = round(subtotal * (1 + impuesto), 2)
        if total <= 0:
            raise CalculoInconsistenteError(f"Costo calculado inválido: {total}")
        return total
