# main.py
# Simulación de operaciones del sistema Software FJ (sin base de datos).
from models.cliente import Cliente
from models.reserva import Reserva
from services.reserva_salas import ReservaSala
from services.alquiler_equipos import AlquilerEquipo
from services.asesoria import Asesoria
from exceptions.excepciones import SoftwareFJError
from utils.logger import obtener_logger

log = obtener_logger()

# Listas internas: reemplazan a la base de datos.
clientes, servicios, reservas = [], [], []


def ejecutar(numero, descripcion, accion):
    """Ejecuta una operación sin detener el programa si algo falla."""
    print(f"\nOperación {numero:02d}: {descripcion}")
    try:
        resultado = accion()
    except SoftwareFJError as error:
        causa = f" | causa: {error.__cause__}" if error.__cause__ else ""
        print(f"  ✗ {type(error).__name__}: {error}{causa}")
        log.error("Op %02d - %s: %s%s", numero, type(error).__name__, error, causa)
    except Exception as error:  # errores inesperados: se registran y se continúa
        print(f"  ✗ Error inesperado: {error}")
        log.exception("Op %02d - error inesperado", numero)
    else:
        print(f"  ✓ {resultado}")
        log.info("Op %02d - OK: %s", numero, resultado)


def registrar_cliente(nombre, documento, correo):
    cliente = Cliente(nombre, documento, correo)
    clientes.append(cliente)
    return cliente


def registrar_servicio(servicio_factory):
    servicio = servicio_factory()
    servicios.append(servicio)
    return servicio


def crear_reserva(cliente, servicio, duracion):
    reserva = Reserva(cliente, servicio, duracion)
    reservas.append(reserva)
    return reserva


def confirmar_y_procesar(reserva, **kwargs):
    reserva.confirmar()
    reserva.procesar(**kwargs)
    return reserva


def main():
    log.info("===== Inicio de la simulación Software FJ =====")

    ejecutar(1, "Registrar cliente válido",
             lambda: registrar_cliente("Ana Gómez", "1065123456", "ana@correo.com"))
    ejecutar(2, "Registrar cliente con correo inválido",
             lambda: registrar_cliente("Luis Pérez", "1065987654", "luis-correo"))
    ejecutar(3, "Registrar cliente con documento inválido",
             lambda: registrar_cliente("Marta Ruiz", "12AB", "marta@correo.com"))
    ejecutar(4, "Crear sala de reuniones válida",
             lambda: registrar_servicio(lambda: ReservaSala("Sala Andes", 80000, 12)))
    ejecutar(5, "Crear equipo con tarifa negativa",
             lambda: registrar_servicio(lambda: AlquilerEquipo("Proyector", -5000, 3)))
    ejecutar(6, "Crear asesoría y equipo válidos",
             lambda: " | ".join(str(registrar_servicio(f)) for f in (
                 lambda: Asesoria("Python POO", 120000, "avanzada"),
                 lambda: AlquilerEquipo("Portátil", 45000, 5))))

    ana = clientes[0]
    sala, asesoria, portatil = servicios[0], servicios[1], servicios[2]

    ejecutar(7, "Reserva exitosa de sala (3 h, IVA 19 %)",
             lambda: confirmar_y_procesar(crear_reserva(ana, sala, 3), impuesto=0.19))
    ejecutar(8, "Reserva de asesoría con descuento del 10 %",
             lambda: confirmar_y_procesar(crear_reserva(ana, asesoria, 2),
                                          impuesto=0.19, descuento=0.10))
    ejecutar(9, "Reserva de sala con 12 horas (fuera de rango)",
             lambda: confirmar_y_procesar(crear_reserva(ana, sala, 12)))

    portatil.cambiar_disponibilidad(False)
    ejecutar(10, "Reservar un equipo no disponible",
             lambda: crear_reserva(ana, portatil, 2))
    ejecutar(11, "Cancelar una reserva ya procesada",
             lambda: reservas[0].cancelar())
    ejecutar(12, "Reserva sin cliente (parámetro faltante)",
             lambda: crear_reserva(None, sala, 2))

    print("\nResumen de reservas en memoria:")
    for reserva in reservas:
        print("  -", reserva)
    log.info("===== Fin de la simulación: %d reservas =====", len(reservas))


if __name__ == "__main__":
    main()
