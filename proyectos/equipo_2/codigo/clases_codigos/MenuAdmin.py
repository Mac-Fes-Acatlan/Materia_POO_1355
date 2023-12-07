"""Clase MenuAdmin"""
from AdministradorPersonas import AdministradorPersonas
from typing import Union
from AdministradorProductos import AdministradorProducto
import pandas as pd
class MenuAdmin:
    """Clase que funciona como el flujo para administradores"""
    @staticmethod
    def inicio_menu_admin() -> Union[str,bool]:
        """Metodo que inicia sesion del administrador"""
        admin_personas_obj = AdministradorPersonas()
        print("Bienvenido")
        while True:
            print("¿Desea iniciar sesión o registrarse?")
            print("Ingrese 1 si desea iniciar sesión.",
                "Ingrese 2 si desea registrase.",
                "Ingrese 3 si desea salir: ", sep='\n')
            sesion = int(input(":"))
            if sesion in range(1,4):
                break
            print("Error. Dato incorrecto, pruebe de nuevo.")
        if sesion == 1:
            identificador = admin_personas_obj.inicio_sesion_admin()
        if sesion == 2:
            identificador = admin_personas_obj.registro_admin()
        if sesion == 3:
            identificador = False
        if identificador == False:
            print("Hasta Luego.")
        return identificador
    
    @staticmethod
    def menu_opciones()-> int:
        """Clase que muestra el menu de opciones para el admnistrador"""
        admin_productos_obj = AdministradorProducto()
        print("Bienvenido\n¿Qué desea hacer hoy?")
        while True:
            while True:
                print("Ingrese alguna de las siguientes opciones:",
                    "1) Ver los ingredientes.",
                    "2) Comprar ingredientes.",
                    "3) Salir.", sep = '\n')
                opcion = int(input(":"))
                if opcion in range(1,4):
                    break
                print("Error en el dato, ingrese uno correcto.")
            
            if opcion == 1:
                for fila in admin_productos_obj.lista_ingredientes_df.itertuples(index=False):
                    print(fila)
            elif opcion == 2:
                while True:
                    while True:
                        print("Ingrese el numero del ingrediente a comprar (Ingrese 0 para cancelar):")
                        compra = int(input(":"))
                        if compra in range(0,13):
                            break
                        print("Error, ingrese un dato valido")
                    if compra == 0:
                        break
                    while True:
                        cantidad = float(input("Ingrese la cantidad en kg a comprar:"))
                        if cantidad >= 0:
                            break
                        print("Error, ingrese un dato valido")
                    admin_productos_obj.lista_ingredientes_df.iat[compra-1,3] += cantidad
                    aux_df_dinero = pd.read_csv("archives//ValoresEmpresa.csv")
                    aux_df_dinero.iat[0,0] -= admin_productos_obj.lista_ingredientes_df.iat[compra-1,5]*cantidad
                    if 'Unnamed' in aux_df_dinero.columns:
                        aux_df_dinero = aux_df_dinero.loc[:, ~aux_df_dinero.columns.str.contains('^Unnamed')]
                    if 'Unnamed' in admin_productos_obj.lista_ingredientes_df.columns:
                        admin_productos_obj.lista_ingredientes_df = admin_productos_obj.lista_ingredientes_df.loc[:, ~admin_productos_obj.lista_ingredientes_df.columns.str.contains('^Unnamed')]
                    admin_productos_obj.lista_ingredientes_df.to_csv("archives/IngredientesFinal.csv")
                    aux_df_dinero.to_csv("archives//ValoresEmpresa.csv")
                    while True:
                        reinicio = int(input("Ingrese 1 si desea comprar otra cosa, sino ingrese 2:"))
                        if reinicio in range(1,3):
                            break
                        print("Error, ingrese un dato valido")
                    if reinicio == 2:
                        break
                
            elif opcion == 3:
                break
        print("Hasta luego.")