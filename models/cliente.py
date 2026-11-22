# models/cliente.py
# Cliente con encapsulación de datos personales y validaciones estrictas.
import re
from models.entidad import Entidad
from exceptions.excepciones import ClienteInvalidoError

PATRON_CORREO = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")


class Cliente(Entidad):
    def __init__(self, nombre, documento, correo):
        super().__init__()
        # Las asignaciones pasan por los setters, que validan cada dato.
        self.nombre = nombre
        self.documento = documento
        self.correo = correo

    # --- nombre -----------------------------------------------------------
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ClienteInvalidoError("El nombre debe tener al menos 3 caracteres.")
        self.__nombre = valor.strip()

    # --- documento ----------------------------------------------------------
    @property
    def documento(self):
        # Solo se muestran los últimos 4 dígitos para proteger el dato.
        return "****" + self.__documento[-4:]

    @documento.setter
    def documento(self, valor):
        valor = str(valor).strip()
        if not valor.isdigit() or not 6 <= len(valor) <= 12:
            raise ClienteInvalidoError("El documento debe tener entre 6 y 12 dígitos.")
        self.__documento = valor

    # --- correo -------------------------------------------------------------
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or not PATRON_CORREO.match(valor):
            raise ClienteInvalidoError(f"Correo no válido: {valor!r}")
        self.__correo = valor.lower()

    def describir(self):
        return f"Cliente #{self.id}: {self.nombre} (doc. {self.documento})"
