from clases.producto import Producto
import pandas as pd


class AdministradorProducto:
    def __init__(self, dict_prod_dis: dict, dict_prod_nodisp: dict):
        """
        Metodo constructor

        Args:
            dict_prod_dis (dict): diccionario de productos disponibles
            dict_prod_nodisp (dict): diccionario de productis no disponibles
        """
        self._dict_prod_dis = dict_prod_dis
        self._dict_prod_nodisp = dict_prod_nodisp
        self._dict_productos_eliminados = {}

        self._nombres = []
        self._marcas = []
        self._skus = []
        self._categorias = []
        self._precios = []
        self._status = []

    def flujo_inventario(self, opcion_flujo: int):
        """
        Metodo que permite ejectuar la operacion ,
        indicada desde el menu que se muestra al usuario

        Args:
            opcion_flujo (int): opcion de entrada para el elegir el flujo
        """
        if opcion_flujo == 1:

            nombre = input("Ingrese el nombre del producto: ")
            marca = input("Ingrese la marca del producto: ")
            sku = input("Ingrese el sku del producto: ")
            categoria = input("Ingrese la categoria del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            status = input("Ingrese el status del producto:")

            producto_obj = Producto(nombre, marca, sku, categoria, precio, status)

            if self._validacion_existencia(sku) == True:

                self._dict_prod_dis[sku] = producto_obj

                self._nombres.append(nombre)
                self._marcas.append(marca)
                self._skus.append(sku)
                self._categorias.append(categoria)
                self._precios.append(precio)
                self._status.append(status)

                return {
                    "nombre": self._nombres,
                    "marca": self._marcas,
                    "skus": self._skus,
                    "categorias": self._categorias,
                    "status": self._status,
                }

            else:
                print("El producto ya se encuentra en stock ingresa uno nuevo")

        elif opcion_flujo == 2:

            sku = input("Ingrese el sku del producto a eliminar: ")

            if not self._validacion_existencia(sku) == True:
                self._dict_productos_eliminados[sku] = self._dict_prod_dis[sku]
                del self._dict_prod_dis[sku]

        elif opcion_flujo == 3:

            self._imprimir_dict_disp()

    def _validacion_existencia(self, sku: str):
        """

        Metodo que permite realizar la validacion de un producto
        en la lista asociada en la clase.

        Args:
            sku (str): identificador del producto

        Returns:
            boolean: Valor identificador de exitencia
        """
        if len(self._dict_prod_dis) > 0:
            for _, elemento in self._dict_prod_dis.items():
                if elemento.sku == sku:
                    return False
            return True
        else:
            return True

    def _imprimir_dict_disp(self):

        df_data = pd.read_csv("valores_productos.csv")
        print(df_data.head())

        """
        for index, row in df.iterrows():
            print(row["Columna 1"], row["Columna 2"])
        """
