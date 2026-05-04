import logging
from excepciones.errores import ErrorReserva

class Reserva:

    def __init__(self, cliente, servicio, tiempo):
        try:
            if cliente is None:
                raise ErrorReserva("Cliente no puede ser None")

            if servicio is None:
                raise ErrorReserva("Servicio no puede ser None")

            self.__cliente = cliente
            self.__servicio = servicio
            self.__tiempo = float(tiempo)

            if self.__tiempo <= 0:
                raise ErrorReserva("Tiempo inválido para la reserva")

            self.__estado = "Pendiente"

        except Exception as e:
            logging.error(f"Error creando Reserva: {e}")
            raise

    # Encapsulación
    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def tiempo(self):
        return self.__tiempo

    @property
    def estado(self):
        return self.__estado

    # Lógica de negocio
    def confirmar(self):
        try:
            costo = self.__servicio.calcular_costo(self.__tiempo)
            self.__estado = "Confirmada"
            logging.info(f"Reserva confirmada - Costo: {costo}")
            print(f"Reserva confirmada. Costo total: {costo}")

            return costo

        except Exception as e:
            logging.error(f"Error al confirmar reserva: {e}")
            raise

    def cancelar(self):
        self.__estado = "Cancelada"
        logging.info("Reserva cancelada")
        print("Reserva cancelada")

    def mostrar(self):
        return (
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Tiempo: {self.__tiempo} | "
            f"Estado: {self.__estado}"
        )