from exceptions.excepciones import ClienteInvalidoError, SoftwareFJError

try:
    raise ClienteInvalidoError("El correo está vacío")
except SoftwareFJError as error:          # la clase base captura a sus hijas
    print("Capturada:", type(error).__name__, "-", error)