import logging
import os


def configurar_logger():
    """
    Configura el registro de eventos y errores en un archivo físico
    y en la consola, cumpliendo con el requerimiento de la guía.
    """
    # Aseguramos que la ruta para el log exista
    ruta_log = os.path.join(os.path.dirname(__file__), '..', 'operaciones.log')

    # aqui tenemos la Configuración base del logger
    logger = logging.getLogger("SoftwareFJ")
    logger.setLevel(logging.DEBUG)

    # aca pusimos la parte que Evita la duplicidad de manejadores si se llama la función varias veces
    if not logger.handlers:
        # Formato del mensaje: Fecha, Nivel, Mensaje
        formato = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # primero pusimos el manejador para archivo (Registro permanente de errores)
        file_handler = logging.FileHandler(ruta_log, encoding='utf-8')
        file_handler.setLevel(logging.ERROR)  # Solo errores y críticos al archivo
        file_handler.setFormatter(formato)

        # aca esta el manejador para consola (Seguimiento de la ejecución)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Información general a la consola
        console_handler.setFormatter(formato)

        # y aqui la opcion para agregar los manejadores al logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


# Instancia global para ser usada en todo el proyecto
log_sistema = configurar_logger()