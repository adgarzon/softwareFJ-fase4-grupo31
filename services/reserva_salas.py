<<<<<<< HEAD
# services/reserva_salas.py
from models.servicio import Servicio
from exceptions.excepciones import ServicioInvalidoError


class ReservaSala(Servicio):
    def __init__(self, nombre, tarifa_hora, capacidad, disponible=True):
        super().__init__(nombre, tarifa_hora, disponible)
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ServicioInvalidoError("La capacidad de la sala debe ser un entero positivo.")
        self._capacidad = capacidad

    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or not 1 <= horas <= 8:
            raise ServicioInvalidoError("Una sala se reserva entre 1 y 8 horas.")

    def costo_base(self, horas):
        return self._tarifa_base * horas

    def describir(self):
        return f"Sala '{self.nombre}' ({self._capacidad} personas) - ${self._tarifa_base:,.0f}/hora"
=======

>>>>>>> 5073abf957aa3d2c45f87eddf12b3071b1284540
