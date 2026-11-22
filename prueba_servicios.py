from services.reserva_salas import ReservaSala
from services.alquiler_equipos import AlquilerEquipo
from services.asesoria import Asesoria

servicios = [
    ReservaSala("Sala Andes", 80000, 12),
    AlquilerEquipo("Portátil", 45000, 5),
    Asesoria("Python POO", 120000, "avanzada"),
]

# Polimorfismo: el mismo mensaje, tres comportamientos distintos.
for servicio in servicios:
    print(servicio.describir(), "->", servicio.calcular_costo(2))

# Variantes del mismo método (sobrecarga con parámetros opcionales).
sala = servicios[0]
print("Base:", sala.calcular_costo(2))
print("Con IVA:", sala.calcular_costo(2, impuesto=0.19))
print("IVA y descuento:", sala.calcular_costo(2, impuesto=0.19, descuento=0.10))