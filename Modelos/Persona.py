from abc import ABC, abstractmethod
import logging

class Persona(ABC):

    def __init__(self, nombre):
        try:
            if not isinstance(nombre, str) or not nombre.strip():
                raise ValueError("Nombre inválido")

            self.__nombre = nombre.strip()

        except Exception as e:
            logging.error(f"Error en Persona: {e}")
            raise

    # Encapsulación
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Nombre inválido")
        self.__nombre = valor.strip()

    @abstractmethod
    def mostrar_info(self):
        pass