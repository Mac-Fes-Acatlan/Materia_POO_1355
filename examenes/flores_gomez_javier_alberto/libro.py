import pandas as pd


class Libro:
    def __init__(self, titulo: str, autor: str, genero: str, cantidad_copias, isbn):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._cantidad_copias = cantidad_copias
        self._isbn = isbn
        if cantidad_copias != 0:
            self._estado = "Disponible"
        else:
            self._estado = "Ocupado"

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def genero(self):
        return self._genero

    @property
    def cantidad_copias(self):
        return self._cantidad_copias

    @property
    def isbn(self):
        return self._isbn

    @property
    def estado(self):
        return self._estado

    def _cambiar_estado(self, dataframe: pd.DataFrame, index):
        if self._estado == "Disponible":
            self._cantidad_copias -= 1
            dataframe.iloc[index, 3] = self._cantidad_copias
            dataframe.to_csv("list_of_books.csv", index=False)
            if self._cantidad_copias == 0:
                self._estado = "Ocupado"

    def _devolver_libro(self, dataframe: pd.DataFrame, index):
        self._cantidad_copias += 1
        dataframe.iloc[index, 3] = self._cantidad_copias
        dataframe.to_csv("list_of_books.csv", index=False)
        if self._estado == "Ocupado":
            self._estado = "Disponible"
            
    def mostrar_libro(self):
        print(f"Titulo: {self._titulo}")
        print(f"Autor: {self._autor}")
        print(f"Genero: {self._genero}")
        print(f"ISBN: {self._isbn}")
