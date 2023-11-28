"""Clase AdministradorPedidos"""
import pandas as pd
from datetime import datetime
from Menu import Menu
from AdministradorProductos import AdministradorProducto

class AdministradorPedidos:
    """Clase que administra los df de pedidos e inventario"""
    _pedidos_df = pd.read_csv("archives//Pedidos.csv")
    
    def __init__(self) -> None:
        pass
    
    @property
    def pedidos_df(self):
        return self._pedidos_df
    @pedidos_df.setter
    def pedidos_df(self,new_df):
        self._pedidos_df = new_df
        
    def imprimir_pedidos(self, 
                        usuario:str) ->bool:
        """Imprime los pedidos de un usuario"""
        for fila in self._pedidos_df.itertuples(index=False):
            aux = str(fila.usuario)
            if aux == usuario:
                print(fila)
    
    def pedir_orden(self, 
                      usuario:str,
                      menu:Menu) -> bool:
        """Metodo que muestra la interfaz para ordenar"""
        menu.mostrar_menu()
        admin_productos = AdministradorProducto()
        cantidad = [0]*10
        while True:
            while True:
                print("Ingrese el número del producto que desea pedir (Ingrese 0 para cancelar)")
                pedido = int(input(":"))
                if pedido in range(0,11):
                    break
                print("Ingrese un dato válido.")
            if pedido == 0:
                return False
            else:
                while True:
                    cantidad_producto = int(input("Ingrese la cantidad de articulos que desea:"))
                    if cantidad_producto >= 0:
                        cantidad[pedido-1] += cantidad_producto
                        break
                    print("Dato incorrecto.")
            while True:
                print("Si desea pedir otra cosa ingrese 1, sino ingrese 2:")
                confirmar = int(input(":"))
                if confirmar in range(1,3):
                    break
                print("Error en el dato.")
            if confirmar == 2:
                break
        precio = 0.0
        for i in range(len(cantidad)):
            if cantidad[i] != 0:
                precio += menu.menu_df.iloc[i][3]
                if i == 0:
                    admin_productos.lista_ingredientes_df.iat[0,4] -= .2*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[1,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[3,4] -= .05*cantidad[i]
                elif i == 1:
                    admin_productos.lista_ingredientes_df.iat[0,4] -= .2*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[1,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[3,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[2,4] -= .02*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[3,4] -= .05*cantidad[i]
                elif i == 2:
                    admin_productos.lista_ingredientes_df.iat[8,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[7,4] -= .1*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[3,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[9,4] -= .05*cantidad[i]
                elif i == 3:
                    admin_productos.lista_ingredientes_df.iat[0,4] -= .2*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[1,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[5,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[4,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[6,4] -= .05*cantidad[i]
                elif i == 4:
                    admin_productos.lista_ingredientes_df.iat[10,4] -= .2*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[1,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iiat[3,4] -= .05*cantidad[i]
                elif i == 5:
                    admin_productos.lista_ingredientes_df.iat[11,4] -= .2*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[1,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[3,4] -= .05*cantidad[i]
                elif i == 6:
                    admin_productos.lista_ingredientes_df.iat[7,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[1,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[4,4] -= .05*cantidad[i]
                elif i == 7:
                    admin_productos.lista_ingredientes_df.iat[8,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[0,4] -= .2*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[5,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[4,4] -= .05*cantidad[i]
                    admin_productos.lista_ingredientes_df.iat[6,4] -= .05*cantidad[i]
                elif i == 8:
                    admin_productos.lista_ingredientes_df.iiat[13,4] -= .5*cantidad[i]
                elif i ==9:
                    admin_productos.lista_ingredientes_df.iat[12,4] -= .5*cantidad[i]
                admin_productos.lista_ingredientes_df.reset_index(drop=True)
                admin_productos.lista_ingredientes_df.to_csv("archives//IngredientesFinal.csv", index=False)
                aux_df_ventas = pd.read_csv("archives//ValoresEmpresa.csv")
                aux_df_ventas.iat[0,0] += precio
                
                
        aux_df = pd.DataFrame({
            "usuario":[usuario],
            "precio":[precio],
            "1":[cantidad[0]],
            "2":[cantidad[1]],
            "3":[cantidad[2]],
            "4":[cantidad[3]],
            "5":[cantidad[4]],
            "6":[cantidad[5]],
            "7":[cantidad[6]],
            "8":[cantidad[7]],
            "9":[cantidad[8]],
            "10":[cantidad[9]],
            "fecha": [datetime.now()]
        })
        aux_concat_df = pd.concat([self.pedidos_df, aux_df])
        if 'Unnamed' in aux_concat_df.columns:
            aux_concat_df = aux_concat_df.loc[:, ~aux_concat_df.columns.str.contains('^Unnamed')]
        self._pedidos_df = aux_concat_df
        self._pedidos_df.to_csv("archives//Pedidos.csv")
        return True
