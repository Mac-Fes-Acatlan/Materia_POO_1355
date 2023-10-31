class Book:
    def __init__(
        self, 
        titulo:str, 
        genero:str, 
        autor:str, 
        cop_dis:int
    ):

        self._titulo = titulo
        self._genero = genero            
        self._autor = autor
        self._cop_dis = cop_dis

        @property
        def titulo(self):
            return self._titulo

        @titulo.setter
        def titulo(self, valor: str):
            self._titulo = valor

        @property
        def genero(self):
            return self._genero

        @genero.setter
        def genero(self, valor: str):
            self._genero = valor

        @property
        def autor(self):
            return self._autor

        @autor.setter
        def autor(self, valor: str):
            self._autor = valor

        @property
        def cop_dis(self):
            return self._cop_dis

        @cop_dis.setter
        def cop_dis(self, valor: str):
            self._cop_dis = valor


    


