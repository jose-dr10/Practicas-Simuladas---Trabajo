import sys
import os

# En esta sección tenemos la Configuración de rutas
ruta_raiz = os.path.dirname(os.path.abspath(__file__))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

from modelos.cliente import Cliente
from modelos.reserva import Reserva
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria
from excepciones.errores import ErrorSoftwareFJ, ErrorValidacion
from utils.logger import log_sistema


def simular_operaciones():
    print("=== INICIANDO SIMULACIÓN SOFTWARE FJ ===")

    # En esta sección tenemos Listas internas para gestión de objetos
    clientes_db = []
    reservas_db = []

    # aqui tenemos el Catálogo de servicios disponibles
    servicios = {
        "sala": ReservaSala("Sala de Juntas B", 45000),
        "equipo": AlquilerEquipo("Laptop Workstation", 30000),
        "asesoria": Asesoria("Consultoría IA", 80000)
    }

    # aqui tenemos los datos de prueba
    operaciones = [
        {"tipo": "cliente", "datos": ["Jose", "12345", "jose@email.com", "3001234567"]},  # Válido
        {"tipo": "cliente", "datos": ["Kevin", "67890", "correo-invalido", "123"]},  # Inválido (Correo/Tel)
        {"tipo": "reserva", "cliente_idx": 0, "serv": "sala", "horas": 3},  # Válida
        {"tipo": "reserva", "cliente_idx": 0, "serv": "equipo", "horas": -1},  # Inválida (Horas negativas)
        {"tipo": "reserva", "cliente_idx": 99, "serv": "asesoria", "horas": 2},  # Inválida (Cliente inexistente)
        {"tipo": "cliente", "datos": ["Admin", "ID99", "admin@fj.com", "7654321"]},  # Válido
        {"tipo": "reserva", "cliente_idx": 1, "serv": "asesoria", "horas": 5},  # Válida
        {"tipo": "pago", "reserva_idx": 0, "desc": 0.1, "imp": 0.19},  # Válido
        {"tipo": "pago", "reserva_idx": 0, "desc": -0.5, "imp": 0.19},  # Inválido (Cálculo inconsistente)
        {"tipo": "reserva", "cliente_idx": 1, "serv": "equipo", "horas": 2}  # Válida
    ]

    for i, op in enumerate(operaciones, 1):
        print(f"\n> Operación #{i}: {op['tipo'].upper()}")
        try:
            if op["tipo"] == "cliente":
                # Intento de creación de cliente
                nuevo_c = Cliente(*op["datos"])
                clientes_db.append(nuevo_c)
                print(f"Éxito: Cliente {nuevo_c.nombre} registrado.")

            elif op["tipo"] == "reserva":
                # Validación de existencia de cliente antes de reservar
                if op["cliente_idx"] >= len(clientes_db):
                    raise ErrorValidacion("El cliente seleccionado no existe en el sistema.")

                nueva_r = Reserva(f"RES-{i}", clientes_db[op["cliente_idx"]], servicios[op["serv"]], op["horas"])
                nueva_r.confirmar_reserva()
                reservas_db.append(nueva_r)
                print(f"Éxito: Reserva {nueva_r.obtener_resumen()['ID']} confirmada.")

            elif op["tipo"] == "pago":
                reserva = reservas_db[op["reserva_idx"]]
                total = reserva.procesar_pago(op["desc"], op["imp"])
                print(f"Éxito: Pago procesado. Total: ${total}")

        except (ErrorSoftwareFJ, ValueError, TypeError, RuntimeError) as e:
            # Captura de errores específicos y registro en LOGS (Requerimiento 2)
            mensaje_error = f"Error en Op #{i}: {str(e)}"
            log_sistema.error(mensaje_error)
            print(f"CONTROLADO: {mensaje_error}")

        except Exception as e:
            # aqui tenemos Encadenamiento para errores no previstos
            log_sistema.critical(f"FALLO CRÍTICO NO PREVISTO: {str(e)}")

        else:
            # aqui lo que pasa es que Se ejecuta si no hubo excepciones
            log_sistema.info(f"Operación #{i} finalizada con éxito.")

        finally:
            # aqui Se ejecuta siempre
            print(f"Finalización de gestión para operación #{i}.")

    print("\n=== SIMULACIÓN FINALIZADA. REVISE operaciones.log PARA DETALLES ===")


if __name__ == "__main__":
    simular_operaciones()