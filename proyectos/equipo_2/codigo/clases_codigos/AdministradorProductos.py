"""Clase que organiza y modifica el inventario a través de csv y pd"""
import pandas as pd

class AdministradorProducto:
    """Clase que guarda un df de la lista de ingredientes"""
    lista_ingredientes_df = pd.read_csv("archives//IngredientesFinal.csv")
    def __init__(self) -> None:
        pass
