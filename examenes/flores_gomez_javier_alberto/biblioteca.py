import pandas as pd
import copy
from usuario import Usuario
from administrar_dataframes import AdminDataFrameBooks
from libro import Libro
class Biblioteca:
    _df_libros = None
    def __init__(self) -> None:
        pass
    
    def crear_df(self):
        self._df_libros = pd.read_csv("list_of_books.csv")
           
    def prestar_libro(self, 
                     usuario:Usuario,
                     admin_df: AdminDataFrameBooks):
        libro_obj = Libro
        if len(usuario.libros_prestados) >= 3:
            print("No se pueden pedir mas libros puesto que ya tiene un maximo de 3 libros en posesion.")
        else:
            while True:
                print("Bienvenido a la interfaz para pedir prestamos.\nSe le recuerda que solo puede pedir 3 libros simultaneamente")
                libro = input("Ingrese el titulo del libro tal cual esta escrito en mostrar libros (si desea salir ingrese 1):")
                if libro == "1":
                    return 0
                if admin_df.iterar_valores_filas(libro,0) == False:
                    print("Libro no encontrado, vuelva a intentarlo.")
                else:
                    break
            while True:
                print(f"El libro seleccionado es:{admin_df.dataframe.iloc[admin_df._index,0]}")
                confirmar = input("Si quiere este libro ingrese \"1\" sino ingrese \"2\":")
                if confirmar == "1":
                    if admin_df.dataframe.iloc[admin_df._index,3] == 0:
                        print("No hay copias disponibles.")
                    else:
                        libro_obj = Libro(
                            admin_df.dataframe.iloc[admin_df._index,0],
                            admin_df.dataframe.iloc[admin_df._index,1],
                            admin_df.dataframe.iloc[admin_df._index,2],
                            admin_df.dataframe.iloc[admin_df._index,3],
                            admin_df.dataframe.iloc[admin_df._index,4]
                        )
                        usuario.libros_prestados.append(libro_obj)
                        print("Los datos del libro son:")
                        libro_obj.mostrar_libro()
                        libro_obj._cambiar_estado(admin_df.dataframe,
                                                  admin_df.index)
                        print("Libro prestado con exito. Recuerda guardar el ISBN")
                    break
                elif confirmar == "2":
                    print("Que lastima :(")
                    break
                else:
                    print("Ingrese un numero valido")
        
    def reservar_libro(self, 
                     usuario:Usuario,
                     admin_df: AdminDataFrameBooks):
        libro_obj = Libro
        if len(usuario.libros_prestados) >= 3 or usuario.reserva == True:
            if usuario.reserva == True and len(usuario.libros_prestados)<3:
                while True:
                    print("Ya tiene un libro reservado y es:")
                    usuario.libros_reservados.mostrar_libro()
                    eleccion = input("Si desea pedirlo ingrese 1 sino 2:")
                    if eleccion == "1":
                        admin_df.iterar_valores_filas(usuario.libros_reservados.isbn,4)
                        usuario.libros_reservados._cambiar_estado(admin_df.dataframe,
                                                                admin_df.index)
                        usuario.libros_prestados.append(usuario.libros_reservados)
                        usuario.libros_reservados = Libro
                        usuario.reserva = False
                        print("Libro pedido con exito.")
                        return 0
                    elif eleccion == "2":
                        print("Esta bien.")
                        return 0
                    else:
                        print("Ingrese una opcion valida.")
            print("No se pueden reservar libros puesto que ya tiene 3 libros.")
        else:
            while True:
                print("Bienvenido a la interfaz para pedir reservas.")
                libro = input("Ingrese el titulo del libro tal cual esta escrito en mostrar libros (si desea salir ingrese 1):")
                if libro == "1":
                    return 0
                if admin_df.iterar_valores_filas(libro,0) == False:
                    print("Libro no encontrado, vuelva a intentarlo.")
                else:
                    break
            while True:
                print(f"El libro seleccionado es:{admin_df.dataframe.iloc[admin_df._index,0]}")
                confirmar = input("Si quiere reservar este libro ingrese \"1\" sino ingrese \"2\":")
                if confirmar == "1":
                    if admin_df.dataframe.iloc[admin_df._index,3] == 0:
                        print("No hay copias disponibles.")
                    else:
                        libro_obj = Libro(
                            admin_df.dataframe.iloc[admin_df._index,0],
                            admin_df.dataframe.iloc[admin_df._index,1],
                            admin_df.dataframe.iloc[admin_df._index,2],
                            admin_df.dataframe.iloc[admin_df._index,3],
                            admin_df.dataframe.iloc[admin_df._index,4]
                        )
                        print(libro_obj.__dict__)
                        print("Los datos del libro son:")
                        libro_obj.mostrar_libro()
                        usuario._libros_reservados = copy.deepcopy(libro_obj)
                        usuario.reserva = True
                        print("Libro reservado con exito. Recuerda guardar el ISBN")
                    break
                elif confirmar == "2":
                    print("Que lastima :(")
                    break
                else:
                    print("Ingrese un numero valido")
    
    def devolver_libro(self,
                       usuario: Usuario,
                       admin_df: AdminDataFrameBooks
                       ):
        if len(usuario.libros_prestados) == 0:
            print("No tiene libros por devolver.")
        else:
            while True:
                print("Los libros que tiene por devolver son:")
                for i in range(len(usuario.libros_prestados)):
                    usuario.libros_prestados[i].mostrar_libro()
                    print("\n\n")
                seleccion = input("\n\nSi desea devolver alguno, por favor ingrese 1 sino ingrese 2:")
                if seleccion == "1":
                    while True:
                        isbn = input("Ingrese el isbn del libro a devolver, ingrese Salir para salir:")
                        for i in range(len(usuario.libros_prestados)):
                            if usuario.libros_prestados[i].isbn == isbn:
                                while True:
                                    print("Libro encontrado.")
                                    confirmar = input("Si desea regresarlo ingrese 1 sino ingrese 2:")
                                    if confirmar == "1":
                                         admin_df.iterar_valores_filas(usuario.libros_prestados[i].titulo,0)
                                         usuario.libros_prestados[i]._devolver_libro(admin_df.dataframe,
                                                                                    admin_df.index)
                                         usuario.libros_prestados.remove(usuario.libros_prestados[i])
                                         print("Libro regresado con exito.")
                                         return 0
                                    elif confirmar == "2":
                                        print("Adios.")
                                        return 0
                                    else:
                                        print("Ingrese un dato valido.")
                        if isbn == "Salir":
                            return 0
                        else:
                            print("Isbn erroneo, ingreselo correctamente")   
                if seleccion == "2":
                    print("Esta bien")
                    return 0
                else:
                    print("Ingrese una opcion valida.")
        
     