# Interfaz Alimentos

```py
from abc import abstractmethod
from abc import ABCMeta
class AlimentoInt(metaclass = ABCMeta):
    
    @abstractmethod
    def mostrar_caracteristicas(self):
        raise NotImplemented("No se implementó la función.")
```

# Interfaz Organizador

```py
class Organizador:
    def ordenar_alfabeticamente():
        pass
    
    def ordenar_lista():
        pass
    
    def menu():
        pass

    def configurar_datos():
        pass

```

# Interfaz Persona

```py
from abc import abstractmethod
from abc import ABCMeta

class IntPersona(metaclass = ABCMeta):
    @abstractmethod
    def mostrar_datos(self):
        raise NotImplemented("No se implementa la clase.")
    
    @abstractmethod
    def cambiar_datos(self):
        raise NotImplemented("No se implemetna la clase.")
    

```