from models.entidad import Entidad

try:
    Entidad()                              # no se puede instanciar una clase abstracta
except TypeError as error:
    print("Correcto, Entidad es abstracta:")
    print(error)