# Menú

```py
from Alimento import Alimento
from AdministradorProductos import AdministradorProducto
from Ingrediente import Ingrediente
import pandas as pd

class Menu:
    _lista_alimentos = [Alimento]
    
    def __init__(self) -> None:
        pass
    
    @property
    def lista_alimentos(self):
        return self._lista_alimentos
    
    def crear_df(self, 
                 administrador:AdministradorProducto) -> None:
        lista_ingredientes = []
        menu_df = pd.read_csv("archives//MenuHamburguesasDef.csv")
        lista_aux = [menu_df.to_numpy().tolist]
        for i in range(len(lista_aux)):
            lista_ingredientes.clear()
            for j in range(2, len(lista_aux[i])):
                lista_ingredientes.append(self._ubicar_ingrediente(administrador, lista_aux[i][j]))
        self._lista_alimentos.append(Alimento(lista_aux[i][0],
                                                lista_aux[i][1],
                                                lista_ingredientes))

    def mostrar_menu(self) -> None:
        print("El menu es:")
        for i in range(self.lista_alimentos):
            print((i+1) + ") " + self.lista_alimentos[i].nombre + "\tPrecio: $" + self.lista_alimentos[i].calcular_precio())
    
    def mostrar_alimento(self, 
                         alimento:str) -> bool:
        for i in range(len(self.lista_alimentos)):
            if alimento == self.lista_alimentos[i].nombre:
                self.lista_alimentos[i].mostrar_caracteristicas()
                return True
        return False 
    
    def _ubicar_ingrediente(self,
                         administrador:AdministradorProducto,
                         ingrediente:str) -> Ingrediente:
        for i in range(len(administrador.lista_disponible)):
            if ingrediente == administrador.lista_disponible[i].nombre:
                return administrador.lista_disponible[i]
        
        for j in range(len(administrador.lista_no_disponible)):
            if ingrediente == administrador.lista_no_disponible[i].nombre:
                return administrador.lista_no_disponible[i]
```