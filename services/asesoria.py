<<<<<<< HEAD
# services/asesoria.py
from models.servicio import Servicio
from exceptions.excepciones import ServicioInvalidoError

RECARGOS = {"basica": 1.0, "avanzada": 1.5, "experta": 2.0}


class Asesoria(Servicio):
    def __init__(self, nombre, tarifa_hora, nivel, disponible=True):
        super().__init__(nombre, tarifa_hora, disponible)
        if nivel not in RECARGOS:
            raise ServicioInvalidoError(f"Nivel de asesoría desconocido: {nivel!r}")
        self._nivel = nivel

    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or horas <= 0 or horas > 40:
            raise ServicioInvalidoError("Las horas de asesoría deben estar entre 0 y 40.")

    def costo_base(self, horas):
        return self._tarifa_base * horas * RECARGOS[self._nivel]

    def describir(self):
        return f"Asesoría '{self.nombre}' nivel {self._nivel} - ${self._tarifa_base:,.0f}/hora"
=======

>>>>>>> 5073abf957aa3d2c45f87eddf12b3071b1284540
