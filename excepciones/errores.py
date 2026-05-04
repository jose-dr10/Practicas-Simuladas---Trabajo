class ErrorSistema(Exception):
    """Clase base para errores del sistema"""
    pass


class ErrorValidacion(ErrorSistema):
    """Errores de validación de datos"""
    pass


class ErrorReserva(ErrorSistema):
    """Errores relacionados con reservas"""
    pass