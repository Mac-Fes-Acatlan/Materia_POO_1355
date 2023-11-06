from .book import Book
from .administrador_biblioteca import adminBiblio
import pandas as pd
class Autor:
    def __init__(self, nombre:str):
        self._nombre=nombre

        self._titulos = []
        self._generos = []
        self._autores = []
        self._copi_dis = []

    def autor_obras(self, opc:int):
        if opc == 1:
            titulo = input("Ingrese el titulo : ")
            genero = input("Ingrese el genero del libro: ")
            autor = input("Ingrese el autor: ")
            cop_dis = input(int("Ingrese las copias dispinibles: "))
            libro_obj = Book(titulo, genero, autor, cop_dis)
            if self._validacion_existencia(autor) == True:

                self._libro_dis[autor] = libro_obj

                self._titulos.append(titulo)
                self._generos.append(genero)
                self._autores.append(autor)
                self._copi_dis.append(cop_dis)
                

                return {
                    "titulo": self._titulos,
                    "genero": self._generos,
                    "autor": self._autores,
                    "copias disponibles": self._copi_dis,
                    
                }
            
            else:
                print("El producto ya se encuentra en stock ingresa uno nuevo")

        elif opc == 2:

            titulo = input("Ingrese el titulo del libro a eliminar: ")

            if not self._validacion_existencia(autor) == True:
                self._libro_eliminados[autor] = self._libro_dis[autor]
                del self._libro_dis[autor]
                
        elif opc == 3:

            self._imprimir_libro_disp()
    def _validacion_existencia(self, titulo: str):
        
        if len(self._libro_dis) > 0:
            for _, elemento in self._libro_dis.items():
                if elemento.titulo == titulo:
                    return False
            return True
        else:
            return True
    def _imprimir_libro_disp(self):

        df_data = pd.read_csv("tabla_libros.csv")
        print(df_data.head())

        """
        for index, row in df.iterrows():
            print(row["Columna 1"], row["Columna 2"])
        """