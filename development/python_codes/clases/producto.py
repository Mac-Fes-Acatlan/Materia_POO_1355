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
