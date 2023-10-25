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
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, valor: str):
        self._marca = valor

    @property
    def sku(self):
        return self._sku
    @sku.setter
    def sku(self, valor: str):
        self._sku = valor

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, valor: str):
        self._categoria = valor

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, valor: float):
        self._precio = valor

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
        self._dict_productos_eliminados={}

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
                self._dict_prod_dis[sku]=producto_obj
            else:
                print('El producto ya se encuentra en stock ingresa uno nuevo')

        elif opcion_flujo == 2:
            sku = input("Ingrese el sku del producto a eliminar: ")
            if not self._validacion_existencia(sku) == True:
                self._dict_productos_eliminados[sku]=self._dict_prod_dis[sku]
                del self._dict_prod_dis[sku]
        
        elif opcion_flujo==3:
            pass

    def _validacion_existencia(self, sku:str):
        if len(self._dict_prod_dis)>0:
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
            print("\tEl nombre del producto es:")
            print("\tLa marca es:")
        print("================") 



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
