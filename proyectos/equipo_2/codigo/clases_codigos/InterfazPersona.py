"""Clase abstracta para persona"""
from abc import abstractmethod
from abc import ABCMeta

class IntPersona(metaclass = ABCMeta):
    @abstractmethod
    def mostrar_datos(self):
        """Metodo que mostrara datos"""
        raise NotImplemented("No se implementa la clase.")
    @abstractmethod
    def cambiar_datos(self):
        """Metodo que cambiara los datos el usuario"""
        raise NotImplemented("No se implemetna la clase.")
