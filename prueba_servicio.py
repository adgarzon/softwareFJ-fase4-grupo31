from models.servicio import Servicio

try:
    Servicio("Genérico", 1000)
except TypeError as error:
    print("Servicio no se instancia directamente:")
    print(error)