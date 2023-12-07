"""Clase AdministradorPersonas"""
import pandas as pd
from typing import Union

class AdministradorPersonas:
    """Clase que administra df de personas"""
    def __init__(self) -> None:
        pass

    _df_admin = pd.read_csv("archives//Administradores.csv")

    _df_cliente = pd.read_csv("archives//Clientes.csv")

    def mostrar_administradores(self):
        """Metodo que muestra administradores"""
        self._df_admin.head(len(self._df_admin))

    def mostrar_clientes(self):
        """Metodo que muestra los clientes"""
        self._df_cliente.head(len(self._df_cliente))

    def inicio_sesion_admin(self) -> Union[str,bool]:
        """Metodo que inicia la sesion como administrador"""
        while(True):
            print("Ingrese sus datos de inicio de sesión: (ingrese 3 para cerrar el programa)")
            user_attempt = str(input("Usuario: "))
            if user_attempt == "3" :
                return False
            pass_attempt = str(input("Contraseña: "))

            for fila in self._df_admin.itertuples(index=False):
                aux_str = str(fila.usuario)
                if aux_str == user_attempt :
                    aux_str = str(fila.password)
                    if aux_str == pass_attempt :
                        return fila.usuario
            print("Error a la hora de ingresar el usuario o contraseña")
    
    def inicio_sesion_cliente(self) -> Union[bool, int]:
        """Metodo que inicia la sesion del cliente"""
        while(True):
            print("Ingrese sus datos de inicio de sesión: (ingrese 3 para cerrar el programa)")
            user_attempt = str(input("Usuario: "))
            if user_attempt == "3" :
                return False
            pass_attempt = str(input("Contraseña: "))


            for fila in self._df_cliente.itertuples(index=False):
                aux_str = str(fila.usuario)
                if aux_str == user_attempt :
                    aux_str = str(fila.password)
                    if aux_str == pass_attempt :
                        return fila.usuario
            print("Error a la hora de ingresar el usuario o contraseña")


    def registro_admin(self) -> bool:
        """Clase que registra un administrador"""
        while(True):
            print("Ingrese el número de lo que quiere hacer:" ,
                   "1) Nuevo administrador" ,
                   "2) Salir" , 
                   sep = "\n")

            x = int(input(":"))

            if x == 1:

                aux = True

                while aux == True:
                    nuevo_usuario = str(input("Ingrese el usuario del administrador: (ingrese 3 para cancelar la operación)"))

                    if nuevo_usuario == "3" :
                        return False
                    
                    for fila in self._df_admin.itertuples(index=False):
                        aux_usuario = str(fila.usuario)
                        if aux_usuario == nuevo_usuario :
                            print("El usuario ya está en uso, ingrese uno nuevo.")
                            aux = True
                            break

                    nuevo_nombre = str(input("Ingrese el nombre del administrador: "))

                    nuevo_password = str(input("Ingrese la contraseña del administrador: "))

                    nueva_direccion = str(input("Ingrese la dirección del administrador: "))

                    nuevo_telefono = str(input("Ingrese teléfono del administrador: "))

                    codigo = len(self._df_admin) + 1

                    print("Los datos ingresados fueron:")
                    print(nuevo_nombre)
                    print(nuevo_usuario)
                    print(nuevo_password)
                    print(nueva_direccion)
                    print(nuevo_telefono)
                    print(codigo)

                    print("Si hay algún dato erroneo, favor de ingresar 1, si todos los datos son correctos ingresar 2")

                    while(True):
                        y = int(input(":"))
                        if y == 1:
                            print("Regresando al menú de opciones de usuario")
                            break
                        elif y == 2:
                            df_aux_1 = pd.DataFrame({"nombre":[nuevo_nombre] ,
                                            "usuario": [nuevo_usuario],
                                            "password": [nuevo_password],
                                            "dirección": [nueva_direccion],
                                            "teléfono": [nuevo_telefono],
                                            "código": [codigo]})
                            df_aux_2 = pd.concat([self._df_admin, df_aux_1])
                            if 'Unnamed' in df_aux_2.columns:
                                df_aux_2 = df_aux_2.loc[:, ~df_aux_2.columns.str.contains('^Unnamed')]
                            self._df_admin = df_aux_2
                            self._df_admin.to_csv("archives//Administradores.csv")
                            break
                        else :
                            print("Dato no válido. Regresando a la opción de selección.")
                    return True
            elif x == 2:
                break

            else :
                print("Dato no válido. Regresando a la opción de selección.")

                return True       

    def registro_clientes(self) -> Union[bool, str]:
        """Clase que registra clientes"""
        while(True):
            print("Ingrese el número de lo que quiere hacer:" ,
                   "1) Nuevo cliente" ,
                   "2) Salir" , 
                   sep = "\n")
            x = int(input(":"))
            if x == 1:
                aux = True
                while aux == True:
                    nuevo_usuario = str(input("Ingrese el usuario del administrador: (ingrese 3 para cancelar la operación)"))

                    if nuevo_usuario == "3" :
                        return False
                    aux = False
                    for fila in self._df_cliente.itertuples(index=False):
                        aux_usuario = str(fila.usuario)
                        if aux_usuario == nuevo_usuario :
                            print("El usuario ya está en uso, ingrese uno nuevo.")
                            aux = True
                            break

                nuevo_nombre = str(input("Ingrese el nombre: "))

                nuevo_password = str(input("Ingrese la contraseña: "))

                nuevo_direccion = str(input("Ingrese la dirección: "))

                nuevo_telefono = str(input("Ingrese su teléfono: "))

                nuevo_email = str(input("Ingrese su email: "))
                
                nuevo_num_tarjeta = str(input("Ingrese su numero de tarjeta:"))

                print("Los datos ingresados fueron:")
                print(nuevo_nombre)
                print(nuevo_usuario)
                print(nuevo_password)
                print(nuevo_direccion)
                print(nuevo_telefono)
                print(nuevo_email)
                print(nuevo_num_tarjeta)

                print("Si hay algún dato erroneo, favor de ingresar 1, si todos los datos son correctos ingresar 2")

                while True:
                    y = int(input(":"))
                    if y == 1:
                        print("Regresando al menú de opciones de usuario")
                        break
                    elif y == 2:
                         df_aux_1 = pd.DataFrame({
                                                     "nombre":[nuevo_nombre],
                                                     "usuario":[nuevo_usuario],
                                                     "password":[nuevo_password],
                                                     "dirección":[nuevo_direccion],
                                                     "teléfono":[nuevo_telefono],
                                                     "email":[nuevo_email],
                                                     "num_tarjeta":[nuevo_num_tarjeta]
                                                  })
                                           
                         df_aux_2 = pd.concat([self._df_cliente, df_aux_1], ignore_index=True)
                         if 'Unnamed' in df_aux_2.columns:
                            df_aux_2 = df_aux_2.loc[:, ~df_aux_2.columns.str.contains('^Unnamed')]
                         self._df_cliente = df_aux_2
                         self._df_cliente.to_csv("archives//Clientes.csv")
                         return nuevo_usuario
                    else :
                        print("Dato no válido. Regresando a la opción de selección.")

            elif x == 2:
                return False

            else :
                print("Dato no válido. Regresando a la opción de selección.")