# Clase Alimento

```py
from InterfazAlimentos import AlimentoInt
from Ingrediente import Ingrediente
from typing import List

class Alimento(AlimentoInt):
    
    _precio = float
    _lista_ingredientes = list(Ingrediente)
    def __init__(self,
                 id:int,
                 nombre:str,
                 lista_ingredientes:List[Ingrediente]) -> None:
        self._id = id
        self._nombre = nombre
        self._lista_ingredientes = lista_ingredientes
    
    @property
    def nombre(self):
        return self._nombre
    @property
    def id(self):
        return self._id
    @property
    def lista_ingredientes(self):
        return self._lista_ingredientes
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo_precio
    
    def mostrar_caracteristicas(self):
        print("Id: " + self.id,
              "\nNombre: " + self.nombre,
              "\nIngredientes: ", *self.lista_ingredientes)
        
    def calcular_precio(self) -> float:
        precio_aux = float(0)
        for i in range(self.lista_ingredientes):
            precio_aux += self._lista_ingredientes[i].precio_venta
        self.precio(precio_aux)
        return self.precio
```
