from datetime import datetime


class Reserva:
    """
    Clase que integra Cliente, Servicio, duración y estado.
    Gestiona el ciclo de vida de una reserva en Software FJ.
    """

    def __init__(self, id_reserva, cliente, servicio, duracion_horas):
        self.__id_reserva = id_reserva
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion_horas = duracion_horas
        self.__estado = "PENDIENTE"  # Estados: PENDIENTE, CONFIRMADA, CANCELADA
        self.__fecha_creacion = datetime.now()

    # aqui tenemos los Getters para acceso controlado

    @property
    def estado(self):
        return self.__estado

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    # aqui tenemos Métodos de Gestión

    def confirmar_reserva(self):
        """Cambia el estado a CONFIRMADA si no ha sido cancelada previamente."""
        if self.__estado == "CANCELADA":
            raise RuntimeError(f"No se puede confirmar la reserva {self.__id_reserva} porque ya fue cancelada.")
        self.__estado = "CONFIRMADA"

    def cancelar_reserva(self):
        """Permite cancelar una reserva pendiente o confirmada."""
        if self.__estado == "CANCELADA":
            return  # Ya está cancelada, no hacemos nada
        self.__estado = "CANCELADA"

    def procesar_pago(self, descuento=0, impuesto=0):
        """
        Calcula el costo total delegando la lógica al objeto servicio (Polimorfismo).
        Implementa el requerimiento de parámetros opcionales.
        """
        try:
            # Se asume que el objeto servicio tiene el método calcular_costo
            total = self.__servicio.calcular_costo(self.__duracion_horas, descuento, impuesto)
            return total
        except Exception as e:
            # Este error se propagará para ser capturado por el logger en capas superiores
            raise ValueError(f"Error al procesar el pago de la reserva {self.__id_reserva}: {str(e)}")

    def obtener_resumen(self):
        """Devuelve un resumen detallado de la operación."""
        return {
            "ID": self.__id_reserva,
            "Cliente": self.__cliente.nombre,
            "Servicio": self.__servicio.nombre,
            "Estado": self.__estado,
            "Total Horas": self.__duracion_horas
        }