import logging
from modelos.servicio import Servicio

class Asesoria(Servicio):

    def calcular_costo(self, tiempo, nivel="basico", recargo=0):
        try:
            if tiempo <= 0:
                raise ValueError("El tiempo debe ser mayor a 0")

            base = self.precio_base * tiempo

            if nivel == "avanzado":
                base *= 1.5
            elif nivel == "intermedio":
                base *= 1.2
            elif nivel != "basico":
                raise ValueError("Nivel de asesoría inválido")

            costo_final = base + recargo

            return costo_final

        except Exception as e:
            logging.error(f"Error en Asesoria: {e}")
            raise

    def descripcion(self):
        return "Servicio de asesoría especializada"