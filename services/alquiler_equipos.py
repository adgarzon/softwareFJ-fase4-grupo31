<<<<<<< HEAD
# services/alquiler_equipos.py
from models.servicio import Servicio
from exceptions.excepciones import ServicioInvalidoError


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, tarifa_dia, unidades_disponibles, disponible=True):
        super().__init__(nombre, tarifa_dia, disponible)
        self._unidades = unidades_disponibles

    def validar_parametros(self, dias):
        if not isinstance(dias, int) or not 1 <= dias <= 30:
            raise ServicioInvalidoError("El alquiler de equipos es de 1 a 30 días (entero).")

    def costo_base(self, dias):
        # Política de ejemplo: desde 7 días se cobra 10 % menos por día.
        factor = 0.9 if dias >= 7 else 1.0
        return self._tarifa_base * dias * factor

    def describir(self):
        return f"Equipo '{self.nombre}' - ${self._tarifa_base:,.0f}/día ({self._unidades} unidades)"
=======

>>>>>>> 5073abf957aa3d2c45f87eddf12b3071b1284540
