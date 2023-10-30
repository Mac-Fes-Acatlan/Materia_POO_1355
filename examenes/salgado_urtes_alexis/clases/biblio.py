class Biblioteca:

    def __init__(self):
        self._lista_usuarios = [] # Lista con objetos usuario
        self._lista_autores = [] # Lista con objetos autor
        self._libros = [] # Lista con objetos libros

    # La función recibe un objeto de tipo libro
    def agregar_libro(self,
                      obj_libro):
        for libro in self._libros:
            if libro.titulo == obj_libro.titulo:
                print("Ya existe un libro con ese título, prueba con otro.")
                return
        self._libros.append(obj_libro)
        print("Libro añadido.")

    # En general, las siguientes funciones reciben objetos           
    def agregar_usuario(self,
                        obj_usuario): 
        for usuario in self._lista_usuarios:
            if usuario.nombre == obj_usuario.nombre:
                print("Ya existe un usuario con ese nombre, prueba con otro.")
                return
        self._lista_usuarios.append(obj_usuario)
        print("El usuario se ha agregado.")
    
    def agregar_autores(self, 
                        obj_autor):
        for autor in self._lista_autores:
            if autor.nombre == obj_autor.nombre:
                print("Ya existe un autor con ese nombre, prueba con otro.")
                return
        self._lista_autores.append(obj_autor)

    def buscar_genero(self, 
                      genero: str):
        libros_genero = []
        for libro in self._libros:
            if libro.genero == genero:
                libros_genero.append(libro)
        if len(libros_genero) == 0:
            print("No existen libros con ese género.")
            return
        for libro in libros_genero:
            print(f"{libro._titulo}, {libro._autor}, {libro._genero}, {libro._copias_disp}")

    
    def buscar_autor(self, 
                     autor: str): # Este método me está volviendo loco >:(
        obras = []
        for libro in self._libros:
            if libro.autor == autor:
                obras.append(libro)
        
        if len(obras) == 0:
            print("No hay obras del autor.")
            return

        for libro in obras:
            print(f"{libro._titulo}, {libro._autor}, {libro._genero}, {libro._copias_disp}")

        return

    def buscar_libro(self, 
                     titulo_libro: str):
        for libro in self._libros:
            if libro.titulo == titulo_libro:
                print("El libro se ha hallado.")
                print(f"{libro.titulo}, {libro.autor}, {libro.genero}, {libro.copias_disp}")
                return
            print("El libro no se encuentra en la biblioteca.")
    def __repr__(self) -> str:
        for libro in self._libros:
            print(f"{libro._titulo}, {libro._autor}, {libro._genero}, {libro._copias_disp}")