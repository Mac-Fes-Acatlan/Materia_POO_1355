class Libro:

    def __init__(self, 
                 titulo: str,
                 autor: str,
                 genero: str,
                 copias_disp: int) -> None:
        # En general, los atributos serán privados y solo los podrá modificar la clase
        # Esto aplica para las demás clases
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._copias_disp = copias_disp
        
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        self._titulo = nuevo_titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor: str):
        self._autor = autor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, nuevo_genero: str):
        self._genero = nuevo_genero

    @property
    def copias_disp(self):
        return self._copias_disp

    def restar_unidad(self):
         if self._copias_disp > 0:
                self._copias_disp -= 1
                return
         print("No quedan más copias del libro.")
         return
    
    def sumar_unidad(self):
        self._copias_disp += 1
        return