class Producto:
    def __init__(
        self,
        nombre: str,
        marca: str,
        sku: str,
        categoria: str,
        precio: float,
        status: str,
    ):
        self._nombre = nombre
        self._marca = marca
        self._sku = sku
        self._categoria = categoria
        self._precio = precio
        self._status = status

        @property
        def status(self):
            return self._status

        @status.setter
        def status(self, valor: str):
            self._status = valor


class AdministradorProducto:
    def __init__(self, dict_prod_dis: dict, dict_prod_nodisp: dict):
        self._dict_prod_dis = dict_prod_dis
        self._dict_prod_nodisp = dict_prod_nodisp

    def flujo_inventario(self, opcion_flujo: int):
        if opcion_flujo == 1:
            nombre = input("Ingrese el nombre del producto: ")
            marca = input("Ingrese la marca del producto: ")
            sku = input("Ingrese el sku del producto: ")
            categoria = input("Ingrese la categoria del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            status = input("Ingrese el status del producto:")
            producto_obj = Producto(nombre, marca, sku, categoria, precio, status)
            print(producto_obj.__dict__)
        elif opcion_flujo == 2:
            pass
        else:
            pass


dict_producto_disponible = {}
dict_producto_nodisponible = {}
administrador_obj = AdministradorProducto(
    dict_producto_disponible, dict_producto_nodisponible
)
opc = 0
while opc != 4:
    while True:
        print("Bienvenido al menu")
        print("1. Agregar producto.")
        print("2. Eliminar Producto.")
        print("3. Generar Informe.")
        print("4. Salir.")
        opc = int(input("Seleccionar opcion: "))
        if opc in range(1, 5):
            break
        print("Opcion no valida")
    administrador_obj.flujo_inventario(opc)
