class Autor:

    def __init__(self, 
                 nombre_autor: str) -> None:
        
        self._nombre_autor = nombre_autor
        self._obras = []

    @property
    def nombre(self):
        return self._nombre_autor
    
    @nombre.setter
    def nombre(self, 
               nuevo_nombre):
        self._nombre_autor = nuevo_nombre

    def agregar_obras(self, 
                      lista_libros: list):
        for libro in lista_libros:
            self._obras.append(libro)