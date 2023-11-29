'''Clase que funciona para modelar un ingrediente de un csv'''
from InterfazAlimentos import AlimentoInt
class Ingrediente(AlimentoInt):
    """Clase que almacena datos de los ingredientes"""
    def __init__(self,
                 nombre:str,
                 cantidad:float,
                 tipo:str,
                 precio_venta:float,
                 precio_compra:float,
                 ) -> None:
        self._nombre = nombre
        self._cantidad = cantidad
        self._tipo = tipo
        self._precio_venta = precio_venta
        self._precio_compra = precio_compra
        self._disponibilidad = self.validar_disponibilidad()
    @property
    def nombre(self):
        """get nombre"""
        return self._nombre
    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre
    @property
    def cantidad(self):
        """get cantidad"""
        return self.cantidad
    @cantidad.setter
    def cantidad(self, new_cantidad):
        self._cantidad = new_cantidad
    @property
    def tipo(self):
        """get tipo"""
        return self._tipo
    @tipo.setter
    def tipo(self, new_tipo):
        self._tipo = new_tipo
    @property
    def precio_venta(self):
        """get precio_venta"""
        return self._precio_venta
    @precio_venta.setter
    def precio_venta(self, new_precio_venta):
        self._precio_venta = new_precio_venta
    @property
    def precio_compra(self):
        """get precio_compra"""
        return self._precio_compra
    @precio_compra.setter
    def precio_compra(self, new_precio_compra):
        self._precio_compra = new_precio_compra
    @property
    def disponibilidad(self):
        """get disponibilidad"""
        return self._disponibilidad  
    
    def validar_disponibilidad(self) -> bool:
        """Metodo que verifica disponibilidad"""
        if self._cantidad > 0:
            return True
        return False
    
    def mostrar_caracteristicas(self):
        """Muestra caracteristicas el ingrediente"""
        print(self.__dict__())  
