# models/entidad.py
# Clase abstracta que representa cualquier entidad general del sistema.
from abc import ABC, abstractmethod
import itertools


class Entidad(ABC):
    _contador = itertools.count(1)   # genera identificadores consecutivos

    def __init__(self):
        self._id = next(Entidad._contador)   # atributo protegido

    @property
    def id(self):
        """Identificador de solo lectura."""
        return self._id

    @abstractmethod
    def describir(self):
        """Cada entidad debe saber describirse (polimorfismo)."""

    def __str__(self):
        return self.describir()
