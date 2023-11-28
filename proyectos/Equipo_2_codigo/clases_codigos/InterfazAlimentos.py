"""Clase abstracta para alimentos"""
from abc import abstractmethod
from abc import ABCMeta
class AlimentoInt(metaclass = ABCMeta):
    """Clase abstracta"""
    @abstractmethod
    def mostrar_caracteristicas(self):
        """Metodo que mostrara caracteristicas del alimento"""
        raise NotImplemented("No se implementó la función.")
