import logging
from modelos.persona import Persona
from excepciones.errores import ErrorValidacion

class Cliente(Persona):

    def __init__(self, nombre, correo):
        super().__init__(nombre)
        try:
            if not isinstance(correo, str) or "@" not in correo or not correo.strip():
                raise ErrorValidacion("Correo inválido")

            self.__correo = correo.strip()

        except Exception as e:
            logging.error(f"Error en Cliente: {e}")
            raise

    # Encapsulación del correo
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or not valor.strip():
            raise ErrorValidacion("Correo inválido")
        self.__correo = valor.strip()

    def mostrar_info(self):
        return f"Cliente: {self.nombre} | Correo: {self.__correo}"