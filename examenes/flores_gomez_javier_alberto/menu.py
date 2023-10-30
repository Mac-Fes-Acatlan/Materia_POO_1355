from usuario import Usuario
from administrar_dataframes import AdminDataFrameBooks
from biblioteca import Biblioteca
class MenuUsuario:
    def __init__(self,
                 biblioteca: Biblioteca) -> None:
        self._biblioteca = biblioteca
        self._admin_dataframes = AdminDataFrameBooks(self._biblioteca._df_libros)
    @property
    def biblioteca(self):
        return self._biblioteca
    
    def _menu_inicial(self,
                     usuario_obj, 
                     ):
        print(f"Bienvenido {usuario_obj.nombre_usuario}.")
        while True:
            while True:
                print("Ingrese el numero de lo que desee hacer:")
                print("1) Mostrar libros.\n2) Pedir prestamo de libro.\n3) Pedir reserva de libro.\n4) Devolver libro.\n5) Salir.")
                eleccion_accion = int(input(":"))
                if eleccion_accion in range(1,6):
                    break
                print("Opcion equivocada, ingrese otra.")
            if eleccion_accion == 5:
                return 0
            else:
                self._opcion(eleccion_accion, usuario_obj)
    
    def _opcion(self, 
                eleccion:int, 
                usuario:Usuario):
        if eleccion == 1:
            self._admin_dataframes.mostrar_libros()
            print("Estos son los libros disponibles en la biblioteca.")
            print("Si va a pedir uno, por favor tenga a la mano su ISBN")
        elif eleccion == 2:
            self._biblioteca.prestar_libro(usuario,self._admin_dataframes)
        elif eleccion == 3:
            self._biblioteca.reservar_libro(usuario, self._admin_dataframes)
        else:
            self._biblioteca.devolver_libro(usuario, self._admin_dataframes)
           
    def _validar_usuario(self):
        while True:
            usuario = str(input("Ingrese su nombre de usuario:"))
            password = str(input("Ingrese su contraseña:"))
            if usuario != "Javier" and usuario != "Josue":
                    print("Usuario no existente, ingrese otro.")
            else:
                if not password == "1234A":
                    print("Contraseña incorrecta, ingrese otra.")
                else:
                    if usuario == "Javier":
                        codigo_user = 1
                    else:
                        codigo_user = 2
                    usuario_obj = Usuario(usuario,password,codigo_user)
                    return usuario_obj