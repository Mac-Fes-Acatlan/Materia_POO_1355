#Clase persona
from InterfazPersona import IntPersona
import abc
class Persona(IntPersona):
    #Clase que funciona para guardar los datos de las personas
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
        while True:
            print("Ingrese el número del dato que desea cambiar:",
                  "1) Nombre",
                  "2) Usuario",
                  "3) Contraseña",
                  "4) Dirección",
                  "5) Teléfono",
                  "6) Salir",
                  sep="\n")

            x = int(input(":"))

            if x == 1:
                print("El nombre anterior es:" + self.nombre)
                nuevo_nombre = str(input("Ingrese el nuevo nombre (ingrese el nombre antiguo si no desea cambiarlo)"))
                self.nombre = nuevo_nombre
            elif x == 2:
                print("El usuario anterior es:" + self.usuario)
                nuevo_usuario = str(input("Ingrese el nuevo usuario (ingrese el usuario antiguo si no desea cambiarlo)"))
                self.usuario = nuevo_usuario
            elif x == 3:
                print("La contraseña anterior es:" + self.password)
                nuevo_password = str(input("Ingrese la nueva contraseña (ingrese la contraseña antigua si no desea cambiarlo)"))
                self.password = nuevo_password
            elif x == 4:
                print("La dirección anterior es:" + self.direccion)
                nuevo_direccion = str(input("Ingrese la nueva dirección (ingrese la dirección antigua si no desea cambiarlo)"))
                self.direccion = nuevo_direccion
            elif x == 5:
                print("El teléfono anterior es:" + self.telefono)
                nuevo_telefono = str(input("Ingrese el nuevo teléfono (ingrese el teléfono antiguo si no desea cambiarlo)"))
                self.telefono = nuevo_telefono
            elif x == 6:
                break
            else:
                print("Dato no válido. Regresando a la opción de selección.")