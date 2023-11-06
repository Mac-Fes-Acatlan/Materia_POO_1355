from .administrador_biblioteca import adminBiblio

class User:
    def __init__(
        self, 
        nombre:str,
        id:str,
        tel:int, 
        email:str, 
        prestamo:int,
        multa:int
    ):
        self._nombre=nombre
        self._id=id
        self._tel=tel
        self._email=email
        self._prestamo=[]
        
        
    def solicitar_prestamo(self, num_multa:int):
        pass

    def devolver_libro(self, libro):
        # Implementar la lógica para devolver un libro prestado
        pass

    def consultar_prestamos(self):
        # Implementar la lógica para consultar los libros prestados al usuario
        pass

    def renovar_prestamo(self, libro):
        # Implementar la lógica para renovar el préstamo de un libro
        pass

    def multa_por_atraso(self, libro):
        # Implementar la lógica para calcular una multa por atraso en la devolución de un libro
        pass

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.identificacion})"
