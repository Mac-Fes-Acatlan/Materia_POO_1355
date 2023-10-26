from clases.producto import Producto


class AdministradorProducto:
    def __init__(self, dict_prod_dis: dict, dict_prod_nodisp: dict):
        self._dict_prod_dis = dict_prod_dis
        self._dict_prod_nodisp = dict_prod_nodisp
        self._dict_productos_eliminados = {}

    def flujo_inventario(self, opcion_flujo: int):

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
        if len(self._dict_prod_dis) > 0:
            for _, elemento in self._dict_prod_dis.items():
                if elemento.sku == sku:
                    return False
            return True
        else:
            return True

    def _imprimir_dict_disp(self):
        print("================")
        print("Los productos en el inventario son:")
        for _, producto in self._dict_prod_dis.items():
            print(producto.__dict__)
        print("================")
