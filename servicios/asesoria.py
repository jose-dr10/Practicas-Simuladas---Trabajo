from servicios.servicio import Servicio
from excepciones.errores import ErrorServicio

class Asesoria(Servicio):
    def calcular_costo(self, tiempo, descuento=0, impuesto=0):
        try:
            # aca tenemos lo que son Las asesorías, que suelen tener un IVA fijo
            iva_especial = impuesto if impuesto > 0 else 0.19
            base = self.precio_base * tiempo
            total = base - (base * descuento) + (base * iva_especial)
            return round(total, 2)
        except Exception as e:
            raise ErrorServicio(f"Fallo en cálculo de Asesoría: {str(e)}")

    def descripcion(self):
        return f"Servicio: {self.nombre} (Consultoría técnica profesional)."