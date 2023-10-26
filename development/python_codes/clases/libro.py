from clases.producto import Producto

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
        pasta: str,
    ) -> None:
    
    super().__init__(nombre, marca, sku, categoria, precio, status)
    
    self.paginas = paginas
    self.editorial = editorial
    self.autor = autor
    self.pasta = pasta

libro_obj = Libro(
    paginas,
    editorial,
    pasta,
    autor,
)