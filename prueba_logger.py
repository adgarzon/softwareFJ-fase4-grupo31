from utils.logger import obtener_logger

log = obtener_logger()
log.info("Prueba de registro desde la capa utils")
log.error("Prueba de error registrado")
print("Revise el archivo logs/software_fj.log")