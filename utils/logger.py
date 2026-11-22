# utils/logger.py
# Configura un único registro (log) en archivo para todo el sistema.
import logging
import os

RUTA_LOGS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
ARCHIVO_LOG = os.path.join(RUTA_LOGS, "software_fj.log")


def obtener_logger(nombre="software_fj"):
    """Devuelve un logger que escribe eventos y errores en logs/software_fj.log."""
    os.makedirs(RUTA_LOGS, exist_ok=True)          # crea la carpeta si no existe
    logger = logging.getLogger(nombre)
    if not logger.handlers:                         # evita duplicar manejadores
        logger.setLevel(logging.INFO)
        manejador = logging.FileHandler(ARCHIVO_LOG, encoding="utf-8")
        formato = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s", "%Y-%m-%d %H:%M:%S"
        )
        manejador.setFormatter(formato)
        logger.addHandler(manejador)
    return logger