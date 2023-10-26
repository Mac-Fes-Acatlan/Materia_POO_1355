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


class Libro(Producto):

    def __init__(
        self,
        nombre: str,
        marca: str,
        sku: str,
        categoria: str,
        precio: float,
        status: str,
        paginas: int,
        editorial: str, 
        autor: str,
        pasta: str
        ) -> None:
    
        super().__init__(nombre, marca, sku, categoria, precio, status)
        
        self.paginas = paginas
        self.editorial = editorial
        self.autor = autor
        self.pasta = pasta


libro_obj = Libro("libro,"," ","1234","horror",
    156,"disp",500,
    "persia",
    "fina",
    "Hector"
)

print(libro_obj.__dict__)