# Pedido

```py
from Alimento import Alimento
from Menu import Menu

class Pedido:
    _estatus = str
    def __init__(self,
                 id:int,
                 nombre:str,
                 lista_alimentos:dict(int),
                 menu:Menu) -> None:
        self._id = id
        self._nombre_cliente = nombre
        self._lista_alimentos = lista_alimentos
        self._menu = menu
        self._precio = self._calcular_precio()
        
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, new_id):
        self._id = new_id
    @property
    def lista_alimentos(self):
        return self._lista_alimentos
    @lista_alimentos.setter
    def lista_alimentos(self, new_lista_alimentos):
        self._lista_alimentos = new_lista_alimentos
    @property
    def menu(self):
        return self._menu
    @property
    def precio(self):
        return self._precio
    @property
    def estatus(self):
        return self._estatus
    @estatus.setter
    def estatus(self, new_estatus):
        self._estatus = new_estatus
        
    def _calcular_precio(self) -> float:
        precio = float(0)
        for clave in self.lista_alimentos.keys():
            if self.lista_alimentos.get(clave) !=0:
                for i in range(len(self.menu.lista_alimentos)):
                    if clave == self.menu.lista_alimentos[i].id:
                        precio += self.menu.lista_alimentos[i].precio*self.lista_alimentos.get(clave)
                        break
        return precio
    
    def mostrar_pedido(self) -> None:
        print(
            "El ID del pedido es:\t\t" + self.id,
            "A nombre de:\t\t" + self._nombre_cliente,
            sep ='\n'
        )
        print("Los alimentos son:")
        for clave in self.lista_alimentos.keys():
            if self.lista_alimentos.get(clave) !=0 :
                for i in range(len(self.menu.lista_alimentos)):
                    if self.menu.lista_alimentos[i].id == clave:
                        print(self.menu.lista_alimentos[i].nombre + ": \t\t" + self.lista_alimentos.get(i))
                        break
        print("Total a pagar:\t\t$" + self.precio) 

```
# Administrador de Pedidos

```py
from Pedido import Pedido
import pandas as pd

class AdministradorPedidos:
    _pedidos_df = pd.DataFrame
    
    def __init__(self) -> None:
        pass
    
    @property
    def pedidos_df(self):
        return self._pedidos_df
    
    def crear_df(self) -> bool:
        self.pedidos_df = pd.read_csv("archives//Pedidos.csv")
    
    def mostrar_pedidos(self):
        self.pedidos_df.head(len(self.pedidos_df))
```