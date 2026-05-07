import sys
import os

# Configuración de rutas del proyecto
ruta_raiz = os.path.dirname(os.path.abspath(__file__))

if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

from modelos.cliente import Cliente
from modelos.reserva import Reserva
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria
from excepciones.errores import ErrorSoftwareFJ, ErrorValidacion
from utils.logger import log_sistema


def registrar_cliente(base_clientes, datos_cliente):
    cliente = Cliente(*datos_cliente)
    base_clientes.append(cliente)

    print(f"Cliente registrado correctamente: {cliente.nombre}")
    return cliente


def crear_reserva(base_clientes, base_reservas, servicios, indice_cliente, servicio, horas, codigo):
    if indice_cliente >= len(base_clientes):
        raise ErrorValidacion("Cliente inexistente.")

    reserva = Reserva(
        codigo,
        base_clientes[indice_cliente],
        servicios[servicio],
        horas
    )

    reserva.confirmar_reserva()
    base_reservas.append(reserva)

    print(f"Reserva creada correctamente: {codigo}")
    return reserva


def procesar_pago_reserva(base_reservas, indice_reserva, descuento, impuesto):
    reserva = base_reservas[indice_reserva]

    total = reserva.procesar_pago(descuento, impuesto)

    print(f"Pago realizado con éxito. Total pagado: ${total}")


def ejecutar_simulacion():
    print("===== SOFTWARE FJ - SIMULACIÓN =====")

    clientes = []
    reservas = []

    catalogo_servicios = {
        "sala": ReservaSala("Sala Ejecutiva", 45000),
        "equipo": AlquilerEquipo("PC Gamer", 30000),
        "asesoria": Asesoria("Asesoría Tecnológica", 80000)
    }

    lista_operaciones = [
        ("cliente", ["Jose", "12345", "jose@email.com", "3001234567"]),
        ("cliente", ["Kevin", "67890", "correo-invalido", "123"]),
        ("reserva", 0, "sala", 3),
        ("reserva", 0, "equipo", -1),
        ("reserva", 99, "asesoria", 2),
        ("cliente", ["Admin", "ID99", "admin@fj.com", "7654321"]),
        ("reserva", 1, "asesoria", 5),
        ("pago", 0, 0.1, 0.19),
        ("pago", 0, -0.5, 0.19),
        ("reserva", 1, "equipo", 2)
    ]

    for numero, operacion in enumerate(lista_operaciones, start=1):

        print(f"\n--- Operación {numero} ---")

        try:
            tipo = operacion[0]

            if tipo == "cliente":
                registrar_cliente(clientes, operacion[1])

            elif tipo == "reserva":
                crear_reserva(
                    clientes,
                    reservas,
                    catalogo_servicios,
                    operacion[1],
                    operacion[2],
                    operacion[3],
                    f"RSV-{numero}"
                )

            elif tipo == "pago":
                procesar_pago_reserva(
                    reservas,
                    operacion[1],
                    operacion[2],
                    operacion[3]
                )

        except (ErrorSoftwareFJ, ValueError, TypeError, RuntimeError) as error:
            mensaje = f"Error controlado en operación {numero}: {error}"

            log_sistema.error(mensaje)

            print(mensaje)

        except Exception as error_critico:
            log_sistema.critical(
                f"ERROR CRÍTICO DEL SISTEMA: {error_critico}"
            )

        else:
            log_sistema.info(
                f"Operación {numero} ejecutada correctamente."
            )

        finally:
            print(f"Fin de operación {numero}")

    print("\n===== FIN DE LA SIMULACIÓN =====")


if __name__ == "__main__":
    ejecutar_simulacion()