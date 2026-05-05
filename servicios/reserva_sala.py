from servicios.servicio import Servicio
from excepciones.errores import ErrorServicio


class ReservaSala(Servicio):
    def calcular_costo(self, tiempo, descuento=0, impuesto=0):
        try:
            if tiempo <= 0:
                raise ErrorServicio("La duración de la reserva de sala debe ser mayor a cero.")

            subtotal = self.precio_base * tiempo
            total = subtotal - (subtotal * descuento) + (subtotal * impuesto)
            return round(total, 2)
        except Exception as e:
            raise ErrorServicio(f"Fallo en cálculo de Sala: {str(e)}")

    def descripcion(self):
        return f"Servicio: {self.nombre} (Uso de instalaciones físicas)."