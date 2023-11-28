# Clase Persona 

```python
from InterfazPersona import IntPersona
import abc

class Persona(IntPersona):

    def __init__(self, 
                 nombre: str,
                 usuario: str, 
                 password: str, 
                 direccion: str, 
                 telefono: str
                 ):
        self._nombre = nombre
        self._usuario = usuario
        self._password = password
        self._direccion = direccion
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, new_usuario):
        self._usuario = new_usuario

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, new_direccion):
        self._direccion = new_direccion

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, new_telefono):
        self._telefono = new_telefono

    def mostrar_datos(self) -> None:
        print(self.nombre)
        print(self.usuario)
        print(self.password)
        print(self.direccion)
        print(self.telefono)

    def cambiar_datos(self) -> None:
        while(True):
             print("Ingrese el número del dato que desea cambiar:" ,
                   "1) Nombre" ,
                   "2) Usuario" ,
                   "3) Contraseña" ,
                   "4) Dirección" ,
                   "5) Teléfono" , 
                   "6) Salir" , 
                   sep = "\n")

             x = int(input(":"))

             if x == 1:
                print("El nombre anterior es:" + self.nombre)
                nuevo_nombre = str(input("Ingrese el nuevo nombre (ingrese el nombre antiguo si no desea cambiarlo)"))
                self.nombre(nuevo_nombre)
             elif x == 2:
                 print("El usuario anterior es:" + self.usuario)
                 nuevo_usuario = str(input("Ingrese el nuevo usuario (ingrese el usuario antiguo si no desea cambiarlo)"))
                 self.usuario(nuevo_usuario)
             elif x == 3:
                 print("La contraseña anterior es:" + self.password)
                 nuevo_password = str(input("Ingrese la nueva contraseña (ingrese la contraseña antigua si no desea cambiarlo)"))
                 self.password(nuevo_password)
             elif x == 4:
                 print("La dirección anterior es:" + self.direccion)
                 nuevo_direccion = str(input("Ingrese la nueva dirección (ingrese la dirección antigua si no desea cambiarlo)"))
                 self.direccion(nuevo_direccion)
             elif x == 5:
                 print("El teléfono anterior es:" + self.telefono)
                 nuevo_telefono = str(input("Ingrese el nuevo teléfono (ingrese el teléfono antiguo si no desea cambiarlo)"))
                 self.telefono(nuevo_telefono)
             elif x == 6:
                 break
             else :
                 print("Dato no válido. Regresando a la opción de selección.")
```

# Persona (Admin)

```py
import Persona
import abc

class PersonaCliente(Persona):
    def __init__(self, 
                 nombre: str,
                 usuario: str, 
                 password: str, 
                 direccion: str, 
                 telefono: str,
                 email: str,
                 tarjeta: str
                 ):
        super().__init__(nombre, usuario, password, direccion, telefono)
        self.email = email
        self.tarjeta = tarjeta

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email   
    
    @property
    def tarjeta(self):
        return self._tarjeta

    @tarjeta.setter
    def tarjeta(self, new_tarjeta):
        self._tarjeta = new_tarjeta  
```

# Persona (Cliente)

```py
import Persona
import abc

class PersonaCliente(Persona):
    def __init__(self, 
                 nombre: str,
                 usuario: str, 
                 password: str, 
                 direccion: str, 
                 telefono: str,
                 email: str,
                 tarjeta: str
                 ):
        super().__init__(nombre, usuario, password, direccion, telefono)
        self.email = email
        self.tarjeta = tarjeta

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email   
    
    @property
    def tarjeta(self):
        return self._tarjeta

    @tarjeta.setter
    def tarjeta(self, new_tarjeta):
        self._tarjeta = new_tarjeta  
```

# Clase Administrador de Personas
```py
from InterfazPersona import IntPersona
from Persona import Persona
from PersonaAdmin import PersonaAdmin
from PersonaCliente import PersonaCliente
import pandas as pd

class AdministradorPersonas:

    def __init__(self) -> None:
        pass

    _df_admin = pd.DataFrame

    _df_cliente = pd.DataFrame

    def mostrar_administradores(self):
     self._df_admin = pd.read_csv("development//clases_codigos//archives//Administradores.csv")
     self._df_admin.head(len(self._df_admin))

    def mostrar_clientes(self):
     self._df_cliente = pd.read_csv("development//clases_codigos//archives//Clientes.csv")
     self._df_cliente.head(len(self._df_cliente))

    def inicio_sesion_admin(self) -> None:
        while(True):
            print("Ingrese sus datos de inicio de sesión: (ingrese 3 para cerrar el programa)")
            user_attempt = str(input("Usuario: "))
            pass_attempt = str(input("Contraseña: "))

            if user_attempt == "3" :
                return False

            for i in range(len(self._df_admin)):
                if self._df_admin.iloc[i][1] == user_attempt :
                    if self._df_admin.iloc[i][2] == pass_attempt :
                        aux = True
                        break
                    else :
                        aux = False
                        break

            if aux == True :
                break
            if aux == False :
                print("Error a la hora de ingresar el usuario o contraseña")
            
            return True
    
    def inicio_sesion_cliente(self) -> None:
        while(True):
            print("Ingrese sus datos de inicio de sesión: (ingrese 3 para cerrar el programa)")
            user_attempt = str(input("Usuario: "))
            pass_attempt = str(input("Contraseña: "))

            if user_attempt == "3" :
                return False

            for i in range(len(self._df_cliente)):
                if self._df_cliente.iloc[i][1] == user_attempt :
                    if self._df_cliente.iloc[i][2] == pass_attempt :
                        aux = True
                        break
                    else :
                        aux = False
                        break

            if aux == True :
                break
            if aux == False :
                print("Error a la hora de ingresar el usuario o contraseña")
    
        return True 

    def registro_admin(self) -> bool:

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
                    self.usuario(nuevo_usuario)

                    if nuevo_usuario == "3" :
                        aux = False
                        return False
                    
                    for i in range(len(self._df_admin)):
                        if self._df_admin.iloc[i][1] == nuevo_usuario :
                            print("El usuario ya está en uso, ingrese uno nuevo.")
                            break
                        if i == len(self._df_admin) - 1:
                            aux = False 

                nuevo_nombre = str(input("Ingrese el nombre del administrador: "))
                self.nombre(nuevo_nombre)

                nuevo_password = str(input("Ingrese la contraseña del administrador: "))
                self.password(nuevo_password)

                nuevo_direccion = str(input("Ingrese la dirección del administrador: "))
                self.direccion(nuevo_direccion)

                nuevo_telefono = str(input("Ingrese teléfono del administrador: "))
                self.telefono(nuevo_telefono)

                self.codigo(len(self._df_admin) + 1)

                print("Los datos ingresados fueron:")
                print(self.nombre)
                print(self.usuario)
                print(self.password)
                print(self.direccion)
                print(self.telefono)
                print(self.codigo)

                print("Si hay algún dato erroneo, favor de ingresar 1, si todos los datos son correctos ingresar 2")

                while(True):
                    y = int(input(":"))
                    if y == 1:
                        print("Regresando al menú de opciones de usuario")
                        break
                    elif y == 2:
                         df_aux_1 = pd.DataFrame({"Nombre":self.nombre ,
                                          "usuario": self.usuario,
                                          "password": self.password,
                                          "dirección": self.direccion,
                                          "teléfono": self.telefono,
                                          "código": self.codigo})
                         df_aux_2 = pd.concat([self._df_admin, df_aux_1])
                         self._df_admin = df_aux_2
                    else :
                        print("Dato no válido. Regresando a la opción de selección.")

             elif x == 2:
                 break

             else :
                 print("Dato no válido. Regresando a la opción de selección.")

             return True       

    def registro_clientes(self) -> None:
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
                    self.usuario(nuevo_usuario)

                    if nuevo_usuario == "3" :
                        aux = False
                        return False
                    
                    for i in range(len(self._df_cliente)):
                        if self._df_cliente.iloc[i][1] == nuevo_usuario :
                            print("El usuario ya está en uso, ingrese uno nuevo.")
                            break
                        if i == len(self._df_cliente) - 1:
                            aux = False 

                nuevo_usuario = str(input("Ingrese el usuario del cliente: "))
                self.usuario(nuevo_usuario)

                nuevo_password = str(input("Ingrese la contraseña del cliente: "))
                self.password(nuevo_password)

                nuevo_direccion = str(input("Ingrese la dirección del cliente: "))
                self.direccion(nuevo_direccion)

                nuevo_telefono = str(input("Ingrese teléfono del cliente: "))
                self.telefono(nuevo_telefono)

                nuevo_email = str(input("Ingrese email del cliente: "))
                self.email(nuevo_email)

                nueva_tarjeta = str(input("Ingrese el número de tarjeta del cliente: "))
                self.tarjeta(nueva_tarjeta)

                print("Los datos ingresados fueron:")
                print(self.nombre)
                print(self.usuario)
                print(self.password)
                print(self.direccion)
                print(self.telefono)
                print(self.email)
                print(self.tarjeta)

                print("Si hay algún dato erroneo, favor de ingresar 1, si todos los datos son correctos ingresar 2")

                while(True):
                    y = int(input(":"))
                    if y == 1:
                        print("Regresando al menú de opciones de usuario")
                        break
                    elif y == 2:
                         df_aux_1 = pd.DataFrame({"Nombre":self.nombre ,
                                          "usuario": self.usuario,
                                          "password": self.password,
                                          "dirección": self.direccion,
                                          "teléfono": self.telefono,
                                          "email": self.email,
                                          "núm tarjeta": self.tarjeta})
                         df_aux_2 = pd.concat([self._df_cliente, df_aux_1])
                         self._df_cliente = df_aux_2
                    else :
                        print("Dato no válido. Regresando a la opción de selección.")

             elif x == 2:
                break
             else :
                 print("Dato no válido. Regresando a la opción de selección.")
```