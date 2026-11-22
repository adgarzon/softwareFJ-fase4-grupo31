from models.cliente import Cliente
from exceptions.excepciones import ClienteInvalidoError

cliente = Cliente("Ana Gómez", "1065123456", "ana@correo.com")
print(cliente)                             # usa describir() a través de __str__
print("Documento protegido:", cliente.documento)

try:
    cliente.correo = "sin-arroba"          # el setter valida y rechaza
except ClienteInvalidoError as error:
    print("Rechazado:", error)
print("El correo no cambió:", cliente.correo)