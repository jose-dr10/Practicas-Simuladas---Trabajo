import logging
from modelos.servicio import Servicio

class ReservaSala(Servicio):

    def calcular_costo(self, tiempo, descuento=0, impuesto=0):
        try:
            base = self.precio_base * tiempo

            if descuento < 0 or impuesto < 0:
                raise ValueError("Descuento o impuesto inválido")

            costo_final = base - (base * descuento) + (base * impuesto)
            return costo_final

        except Exception as e:
            logging.error(f"Error en ReservaSala: {e}")
            raise

    def descripcion(self):
        return "Servicio de reserva de salas por horas"