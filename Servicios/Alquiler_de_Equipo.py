import logging
from modelos.servicio import Servicio

class AlquilerEquipo(Servicio):

    def calcular_costo(self, tiempo, seguro=0):
        try:
            if tiempo <= 0:
                raise ValueError("El tiempo debe ser mayor a 0")

            base = self.precio_base * tiempo
            costo_final = base + seguro

            return costo_final

        except Exception as e:
            logging.error(f"Error en AlquilerEquipo: {e}")
            raise

    def descripcion(self):
        return "Servicio de alquiler de equipos tecnológicos"