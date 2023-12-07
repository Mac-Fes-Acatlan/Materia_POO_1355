"""Clase Menu"""
import pandas as pd

class Menu:
    """Clase que almacena el df de alimentos"""
    _menu_df = pd.read_csv("archives//MenuHamburguesasDef.csv", sep = ';')
    
    def __init__(self) -> None:
        pass
    
    @property
    def menu_df(self):
        """get menu_df"""
        return self._menu_df

    def mostrar_menu(self) -> None:
        """Metodo que muestra el menu"""
        print("El menu es:")
        print(self._menu_df.to_string(index = False))
