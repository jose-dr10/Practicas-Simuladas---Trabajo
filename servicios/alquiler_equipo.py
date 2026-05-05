from servicios.servicio import Servicio
from excepciones.errores import ErrorServicio

class AlquilerEquipo(Servicio):
    def calcular_costo(self, tiempo, descuento=0, impuesto=0, seguro=0.05):
        try:
            # aqui tenemos laLógica específica, por lo tanto  se añade un seguro por defecto del 5%
            base = self.precio_base * tiempo
            total = base - (base * descuento) + (base * impuesto) + (base * seguro)
            return round(total, 2)
        except Exception as e:
            raise ErrorServicio(f"Fallo en cálculo de Alquiler: {str(e)}")

    def descripcion(self):
        return f"Servicio: {self.nombre} (Préstamo de hardware especializado)."