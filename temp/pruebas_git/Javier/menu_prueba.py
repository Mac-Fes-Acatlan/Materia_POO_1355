"""Programa con una clase menu"""
class Menu:
    """Clase que funciona como un menu"""
    _seleccion = int(0)
    _bucle = int(0)
    """Lista que recopila los nombres de las opciones, al final siempre debe de ir la opcion de salida"""
    _opciones_lista = ["Primera opcion", "Segunda opcion", "Salir"]

    """No se solicitan atributos de instanciacion """
    def __init__(self):
        pass

    def menu_bucle(self):
        """Metodo que funciona como el menu"""
        
        print("Bienvenido al programa.")
        while True:
            self._desplegar_opciones_bucle()
            
            if self._seleccion != len(self._opciones_lista):
                """Aqui se deben de colocar todas las posibles opciones"""
                if self._seleccion == 1:
                    print("Ejecutando", self._opciones_lista[self._seleccion - 1], "\n")
                    """Print representativo, cambiese por lo que hace la opcion"""
                elif self._seleccion == 2:
                    print("Ejecutando", self._opciones_lista[self._seleccion - 1], "\n")
                    """Print representativo, cambiese por lo que hace la opcion"""
                    
                self._regresar_inicio_bucle()
                
            else:
                break
            if self._bucle == 2:
                break
        return print("\nAdios.")
    
    def _desplegar_opciones_bucle(self)->None:
        """Metodo que despliega las opciones y solicita la que se usara"""
        while True:
            print("\nSeleccione el proceso a realizar:")
            
            """Imprime las opciones en la lista"""
            for i in range(len(self._opciones_lista)):
                print(f"{i+1}) {self._opciones_lista[i]}.")
            
            """Solicita la opcion a usar"""
            self._seleccion = int(input("Ingrese el numero:"))
            if not self._seleccion in range(1, len(self._opciones_lista) + 1):
                print("Dato invalido. Pruebe con otro.")
                
            else:
                break
    
    def _regresar_inicio_bucle(self)->None:
        """Metodo que pregunta si se regresara al inicio o se saldra del programa"""
        while True:
            print("Desea regresar al inicio?")
            self._bucle = int(
                input("1) Regresar al inicio.\n2) Salir.\nIngrese el numero:")
            )
            if self._bucle not in (1, 2):
                print("Dato invalido. Pruebe con otro.\n")
            else:
                break

"""Flujo de prueba"""
menu_obj = Menu()
menu_obj.menu_bucle()
