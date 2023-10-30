class Usuario:

    def __init__(self, 
                 nombre: str) -> None:
        self._nombre = nombre
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, 
               nombre_actualizado: str):
        self._nombre = nombre_actualizado
