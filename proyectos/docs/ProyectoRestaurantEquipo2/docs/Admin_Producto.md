# Clase Administrador de Productos
```py
import pandas as pd
from Ingrediente import Ingrediente

class AdministradorProducto:
    _lista_disponible = [Ingrediente]
    _lista_no_disponible = [Ingrediente]
    def __init__(self) -> None:
        pass
    
    @property
    def lista_disponible(self):
        return self._lista_disponible
    
    @lista_disponible.setter
    def lista_disponible(self, lista:list):
        self._lista_disponible = lista
        
    @property
    def lista_no_disponible(self):
        return self._lista_no_disponible
    
    @lista_no_disponible.setter
    def lista_no_disponible(self, lista:list):
        self._lista_no_disponible = lista
    
    def crear_listas(self) -> None:
        lista_aux = []
        df_ingredientes = pd.read_csv("development//clases_codigos//archives//IngredientesFinal.csv")
        lista_aux = [df_ingredientes.to_numpy().tolist]
        for i in range(len(lista_aux)):
           ingrediente_aux = Ingrediente(lista_aux[i][1],
                                         lista_aux[i][3],
                                         lista_aux[i][2],
                                         lista_aux[i][4],
                                         lista_aux[i][5])
           if ingrediente_aux.disponibilidad == True:
               self._lista_disponible.append(ingrediente_aux)
           else:
               self._lista_no_disponible.append(ingrediente_aux)
    
    def mostrar_disponibles(self) -> None:
        df_disponible = pd.DataFrame(self._lista_disponible)
        df_disponible.head(30)
    
    def mostrar_no_disponible(self) -> None:
        df_no_disponible = pd.DataFrame(self._lista_no_disponible)
        df_no_disponible.head(30)
        
    def modificar_inventario(self) -> bool:
        
        while(True):
            identificador = input("Ingrese el nombre del producto a modificar (Ingrese 0 si desea salir):")
            if  identificador != "0":   
                comprobar = self._encontrar_producto(identificador)
                if comprobar > 0:
                    self._modificar_disponible(comprobar-1)
                elif comprobar < 0:
                    self._modificar_no_disponible((comprobar*-1)-1)
                else:
                    print("Error. El producto ingresado no existe.")
            else:
                return False
                    
    
    def _encontrar_producto(self, 
                            producto:str) -> int:
        for i in range(len(self._lista_disponible)):
            if self._lista_disponible[i].nombre == producto:
                return i+1
        for j in range(len(self._lista_no_disponible)):
            if self._lista_no_disponible[j].nombre == producto:
                return -j-1
        return 0
    
    def _modificar_disponible(self, identificador:int) -> bool:
        while(True):
                print("Opciones a modificar:")
                print("1) Nombre.",
                    "2) Cantidad.",
                    "3) Tipo." ,
                    "4) Precio de venta.", 
                    "5) Precio de compra.",
                    "6) En caso de que desee salir, presione \"6\".",
                    sep = "\n")
                opcion = int(input("Ingrese el dato a cambiar:"))
                if opcion == 1:
                    print("Nombre antiguo: " + self.lista_disponible[identificador].nombre)
                    nuevo_nombre = input("Ingrese el nuevo nombre del producto:")
                    self._lista_disponible[identificador].nombre(nuevo_nombre)
                    print("Sus cambios se realizaron con éxito.")
                elif opcion == 2:
                    print("Cantidad antigua: " + self.lista_disponible[identificador].cantidad)
                    nueva_cantidad = float(input("Ingrese la nueva cantidad del producto (en kg):"))
                    self.lista_disponible[identificador].cantidad(nueva_cantidad)
                    print("Sus cambios se realizaron con éxito.")
                elif opcion == 3:
                    print("Tipo antiguo: " + self.lista_disponible[identificador].tipo)
                    nuevo_tipo = input("Ingrese el nuevo tipo del producto:")
                    self.lista_disponible[identificador].tipo(nuevo_tipo)
                    print("Sus cambios se realizaron con éxito.")
                elif opcion == 4:
                    print("Precio de venta antiguo: $" + self.lista_disponible[identificador].precio_venta)
                    nuevo_precio_venta = float(input("Ingrese el nuevo precio de venta:"))
                    self.lista_disponible[identificador].precio_venta(nuevo_precio_venta)
                    print("Sus cambios se realizaron con éxito.")
                elif opcion == 5:
                    print("Precio de compra antiguo: $" + self.lista_disponible[identificador].precio_compra)
                    nuevo_precio_compra = float(input("Ingrese el nuevo precio de compra:"))
                    self.lista_disponible[identificador].precio_compra(nuevo_precio_compra)
                    print("Sus cambios se realizaron con éxito.")
                elif opcion == 6:
                    print("Adios.")
                    return True
                else:
                    print("Ingrese un dato válido.")
    
    def _modificar_no_disponible(self, identificador:int) -> bool:
        while(True):
                print("Opciones a modificar:")
                print("1) Nombre.",
                    "2) Cantidad.",
                    "3) Tipo." ,
                    "4) Precio de venta.", 
                    "5) Precio de compra.",
                    "6) En caso de que desee salir, presione \"6\".",
                    sep = "\n")
                opcion = int(input("Ingrese el dato a cambiar:"))
                if opcion == 1:
                    print("Nombre antiguo: " + self.lista_no_disponible[identificador].nombre)
                    nuevo_nombre = input("Ingrese el nuevo nombre del producto:")
                    self._lista_no_disponible[identificador].nombre(nuevo_nombre)
                    print("Sus cambios se realizaron con éxito.")
                elif opcion == 2:
                    print("Cantidad antigua: " + self.lista_no_disponible[identificador].cantidad)
                    nueva_cantidad = float(input("Ingrese la nueva cantidad del producto (en kg):"))
                    self.lista_no_disponible[identificador].cantidad(nueva_cantidad)
                    print("Sus cambios se realizaron con éxito.")
                elif opcion == 3:
                    print("Tipo antiguo: " + self.lista_no_disponible[identificador].tipo)
                    nuevo_tipo = input("Ingrese el nuevo tipo del producto:")
                    self.lista_no_disponible[identificador].tipo(nuevo_tipo)
                    print("Sus cambios se realizaron con éxito.")
                elif opcion == 4:
                    print("Precio de venta antiguo: $" + self.lista_no_disponible[identificador].precio_venta)
                    nuevo_precio_venta = float(input("Ingrese el nuevo precio de venta:"))
                    self.lista_no_disponible[identificador].precio_venta(nuevo_precio_venta)
                    print("Sus cambios se realizaron con éxito.")
                elif opcion == 5:
                    print("Precio de compra antiguo: $" + self.lista_no_disponible[identificador].precio_compra)
                    nuevo_precio_compra = float(input("Ingrese el nuevo precio de compra:"))
                    self.lista_no_disponible[identificador].precio_compra(nuevo_precio_compra)
                    print("Sus cambios se realizaron con éxito.")
                elif opcion == 6:
                    print("Adios.")
                    return True
                else:
                    print("Ingrese un dato válido.")
```