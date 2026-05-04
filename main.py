from utils.logger import configurar_logger
from modelos.cliente import Cliente
from modelos.reserva import Reserva
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria
from excepciones.errores import ErrorValidacion, ErrorReserva


def simulacion():

    configurar_logger()

    operaciones = []

    # =========================
    # 1. CLIENTES (válido e inválido)
    # =========================
    try:
        c1 = Cliente("Juan", "juan@mail.com")
        operaciones.append("Cliente válido creado")

        c2 = Cliente("", "error@mail.com")  # ERROR
    except Exception as e:
        operaciones.append(f"Error cliente: {e}")

    # =========================
    # 2. SERVICIOS
    # =========================
    s1 = ReservaSala("Sala VIP", 50)
    s2 = AlquilerEquipo("Proyector", 30)
    s3 = Asesoria("Consultoría", 100)

    operaciones.append("Servicios creados")

    # =========================
    # 3. RESERVAS (válidas e inválidas)
    # =========================
    try:
        r1 = Reserva(c1, s1, 2)
        r1.confirmar()
        operaciones.append(r1.mostrar())

        r2 = Reserva(c1, s2, -1)  # ERROR
        r2.confirmar()

    except Exception as e:
        operaciones.append(f"Error reserva: {e}")

    # =========================
    # 4. MÁS CASOS (simulación obligatoria)
    # =========================
    try:
        r3 = Reserva(c1, s3, 3)
        r3.confirmar()
        operaciones.append(r3.mostrar())

        r4 = Reserva(c1, s1, 5)
        r4.cancelar()
        operaciones.append(r4.mostrar())

    except Exception as e:
        operaciones.append(f"Error general: {e}")

    # =========================
    # RESULTADO FINAL
    # =========================
    print("\n===== RESUMEN DEL SISTEMA =====")
    for op in operaciones:
        print(op)


if __name__ == "__main__":
    simulacion()