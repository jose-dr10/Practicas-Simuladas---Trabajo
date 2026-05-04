from abc import ABC, abstractmethod
import logging

class Servicio(ABC):

    def __init__(self, nombre, precio_base):
        try:
            if not isinstance(nombre, str) or not nombre.strip():
                raise ValueError("Nombre de servicio inválido")

            if not isinstance(precio_base, (int, float)) or precio_base <= 0:
                raise ValueError("Precio base inválido")

            self.__nombre = nombre.strip()
            self.__precio_base = float(precio_base)

        except Exception as e:
            logging.error(f"Error en Servicio: {e}")
            raise

    # Encapsulación
    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio_base(self):
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Precio base inválido")
        self.__precio_base = float(valor)

    # Métodos abstractos (polimorfismo obligatorio)
    @abstractmethod
    def calcular_costo(self, tiempo):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    # Método común reutilizable (base para sobrecarga lógica)
    def validar_tiempo(self, tiempo):
        if not isinstance(tiempo, (int, float)) or tiempo <= 0:
            raise ValueError("Tiempo inválido")