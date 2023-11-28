# Clase Administrador de pedidos 

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

