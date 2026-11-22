from models.cliente import Cliente
from models.reserva import Reserva
from services.reserva_salas import ReservaSala
from exceptions.excepciones import OperacionNoPermitidaError, ReservaInvalidaError

cliente = Cliente("Ana Gómez", "1065123456", "ana@correo.com")
sala = ReservaSala("Sala Andes", 80000, 12)

reserva = Reserva(cliente, sala, 3)
reserva.confirmar()
print("Total:", reserva.procesar())        # IVA del 19 % por defecto
print(reserva)

try:
    reserva.cancelar()                     # ya está PROCESADA
except OperacionNoPermitidaError as error:
    print("Bloqueado:", error)

larga = Reserva(cliente, sala, 12)         # 12 horas: fuera de rango
larga.confirmar()
try:
    larga.procesar()
except ReservaInvalidaError as error:
    print("Error:", error)
    print("Causa original:", error.__cause__)