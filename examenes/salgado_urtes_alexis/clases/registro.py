class RegistroInteracciones: 
    
    def __init__(self, 
                 biblioteca):
        self._libros_prestados = []
        self._libros_devueltos = []
        self.biblioteca = biblioteca # La claase RegistroInteracciones es la clase 'Padre'
                                     # El problema es que me generaba error cuando intentaba interactuar con ella desde aquí XD
                                     # Como los libros, autores y usuarios se guardan allá, lo mejor es tener a la biblio como atributo

    def verificar_existencia_usuario(self, nombre: str):
        for usuario in self.biblioteca._lista_usuarios:
            if usuario.nombre == nombre:
                return True
        return False
    
    def verificar_existencia_libro(self, titulo: str):
        for libro in self.biblioteca._libros:
            if libro.titulo == titulo:
                return True
        return False

    # La función recibe un objeto libro
    def prestar_libro(self, 
                      titulo_libro: str, 
                      nombre_usuario: str):
            # Tenía una verificación del usuario aquí, pero lo cierto es que es más fácil usarlo en el main
            for libro in self.biblioteca._libros:
                if libro.titulo == titulo_libro:
                    if self.ya_prestado(titulo_libro, nombre_usuario):
                        print("Ya tienes ese libro, no se te puede prestar otra vez.")
                        return # Como el usuario ya tiene el libro, no se le puede prestar otra vez. Se salta lo lógica de siquiera verificar que esté disponible.
                    if libro.copias_disp > 0:
                        self._libros_prestados.append((nombre_usuario, libro.titulo)) # Se agrega una tupla para ver quién pidió el libro y cuál libro, por supuesto
                        libro.restar_unidad() # Como se prestó el libro, reducimos en 1 las copias
                        print("El libro se prestó exitosamente.")
                        return
            print("No se pudo prestar el libro, pues no está disponible.")
            return

    def devolver_libro(self, 
                       titulo_libro: str,
                       nombre: str):
        print("Iniciando verificación para devolver el libro")
            # Si se ejecuta lo de abajo, significa que se puede devolver el libro
            # por lo que tenemos que eliminar la tupla de arriba :D (Demasiado siniestro)
            # Al igual que en la función de prestar libro, es mejor hacer la verificación en el main
        for usuario, libro in self._libros_prestados:
            if usuario == nombre and libro == titulo_libro:
                for libro in self.biblioteca._libros:
                    if libro.titulo == titulo_libro:
                        libro.sumar_unidad()
                print("Se ha devuelto el libro.")
                self._libros_devueltos.append((usuario, libro.titulo))
                # Básicamente de cambia de lista :P
                return
        print(f"{nombre} no pidió {titulo_libro}, no se puede devolver.")
        return

    def ya_prestado(self, 
                    titulo_libro: str,
                    nombre_usuario: str) -> None:

        for usuario, libro in self._libros_prestados:
            if usuario == nombre_usuario and libro == titulo_libro:
                return True # La función se usará para asegurar que no se le preste dos veces el libro al mismo usuario
        return False