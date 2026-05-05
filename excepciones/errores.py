class ErrorSoftwareFJ(Exception):
    """
    Clase base para todas las excepciones personalizadas
    del sistema Software FJ.
    """
    def __init__(self, mensaje, codigo_error=None):
        super().__init__(mensaje)
        self.codigo_error = codigo_error
        self.mensaje = mensaje

class ErrorValidacion(ErrorSoftwareFJ):
    """
    Se lanza cuando los datos de entrada
    no cumplen con los requisitos de la guía.
    """
    pass

class ErrorReserva(ErrorSoftwareFJ):
    """
    Se lanza cuando ocurre una operación no permitida en las reservas.
    """
    pass

class ErrorServicio(ErrorSoftwareFJ):
    """
    Se lanza cuando un servicio no está disponible o los
    cálculos de costo no son validos
    """
    pass