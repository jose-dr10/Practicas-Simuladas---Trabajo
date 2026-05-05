from abc import ABC, abstractmethod

class Servicio(ABC):
    """
    Clase abstracta que define la estructura de los servicios
    en Software FJ, cumpliendo con el principio de abstracción.
    """
    def __init__(self, nombre, precio_base):
        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @abstractmethod
    def calcular_costo(self, tiempo, descuento=0, impuesto=0):
        """
        Método abstracto para el cálculo de costos.
        Obliga a implementar polimorfismo en las clases hijas.
        """
        pass

    @abstractmethod
    def descripcion(self):
        """Devuelve una descripción detallada del servicio."""
        pass