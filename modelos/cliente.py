import re
from modelos.persona import Persona

class Cliente(Persona):
    """
    Clase que representa a un cliente en el sistema Software FJ.
    Implementa validaciones robustas y encapsulación de datos personales.
    """
    def __init__(self, nombre, identificacion, correo, telefono):
        # Llamada al constructor de la clase abstracta Persona
        super().__init__(nombre, identificacion)
        self.__correo = None
        self.__telefono = None

        # aqui tenemos la asignación a través de setters para disparar las validaciones iniciales
        self.correo = correo
        self.telefono = telefono

    #aqui lo que tenemos son los Getters y Setters específicos con validaciones
    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self, valor):
        # aqui esta la Validación con expresión regular para un formato de correo estándar
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, valor):
            raise ValueError(f"El formato del correo '{valor}' es inválido.")
        self.__correo = valor
    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, valor):
        # aqui esta la Validación con solo números y longitud mínima de 7 dígitos
        if not str(valor).isdigit() or len(str(valor)) < 7:
            raise ValueError("El teléfono debe contener solo números (mínimo 7 dígitos).")
        self.__telefono = valor

    # aca esta la Implementación de métodos abstractos
    def mostrar_informacion(self):
        """Implementación obligatoria del método de la clase Persona."""
        return f"Cliente: {self.nombre} | ID: {self.identificacion} | Contacto: {self.correo}"
    def validar_registro(self):
        """Verifica que todos los campos esenciales del cliente estén presentes."""
        if all([self.nombre, self.identificacion, self.correo, self.telefono]):
            return True
        return False
    def __str__(self):
        """Representación en cadena para facilitar el registro en logs."""
        return f"[ID: {self.identificacion}] {self.nombre}"
