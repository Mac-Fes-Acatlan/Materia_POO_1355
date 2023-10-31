import pandas as pd


class AdminDataFrame:
    _index = int

    def __init__(self, dataframe) -> None:
        self._dataframe = dataframe

    @property
    def dataframe(self):
        return self._dataframe

    @property
    def index(self):
        return self._index

    def imprimir_dataframe(self):
        aux_dataframe = self._dataframe
        print(aux_dataframe.to_string())

    def iterar_valores_columnas(self, buscar, fila: int) -> bool:
        for i in range(len(self._dataframe)):
            if self._dataframe.iloc[fila, i] == buscar:
                return True
        return False

    def iterar_valores_filas(self, buscar, columna: int) -> bool:
        for i in range(len(self._dataframe)):
            if self._dataframe.iloc[i, columna] == buscar:
                self._index = i
                return True
        return False


class AdminDataFrameBooks(AdminDataFrame):
    def mostrar_libros(self):
        print(self._dataframe.head(51))
