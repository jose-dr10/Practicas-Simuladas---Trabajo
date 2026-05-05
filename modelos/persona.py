from abc import ABC, abstractmethod


class Persona(ABC):
    """
    Clase abstracta que representa una entidad general (Persona)
    dentro del sistema de Software FJ.
    """

    def __init__(self, nombre, identificacion):
        self.__nombre = nombre
        self.__identificacion = identificacion

    # aqui tenemos los  Getters y Setters con Encapsulación

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena de texto válida.")
        self.__nombre = valor

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        if not str(valor).isalnum():
            raise ValueError("La identificación debe ser alfanumérica.")
        self.__identificacion = valor

    # aqui tenemos los  Métodos Abstractos

    @abstractmethod
    def mostrar_informacion(self):
        """Método que debe ser implementado por las subclases."""
        pass

    @abstractmethod
    def validar_registro(self):
        """Define la lógica de validación específica de la entidad."""
        pass