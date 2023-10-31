class Usuario:
    def __init__(self, nombre: str, cuenta: str, status: str, libros_prestados: int):
        self._nombre = nombre
        self._cuenta = cuenta
        self._status = status
        self._libros_prestados = libros_prestados

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def cuenta(self):
        return self._cuenta

    @cuenta.setter
    def cuenta(self, nueva_cuenta):
        self._cuenta = nueva_cuenta

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, nuevo_status):
        self._status = nuevo_status

    @property
    def libros_prestados(self):
        return self._libros_prestados

    @libros_prestados.setter
    def libros_prestados(self, nuevos_libros_prestados):
        self._libros_prestados = nuevos_libros_prestados

    @classmethod
    def crear_usuario(cls, nombre, cuenta, status, libros_prestados):
        nuevo_usuario = cls(nombre, cuenta, status, libros_prestados)
        return nuevo_usuario

class Libro:
    def __init__(self):
        self.libros = [
            {"titulo": "El arte de amar", "autor": "Eric Fromm", "genero": "Filosofía", "copias_disponibles": 5},
            {"titulo": "Álgebra Lineal", "autor": "Grossman", "genero": "Educación", "copias_disponibles": 3},
            {"titulo": "Leviatán", "autor": "Thomas Hobbes", "genero": "Derecho", "copias_disponibles": 2}
        ]

    def obtener_libro_por_titulo(self, titulo):
        for libro in self.libros:
            if libro["titulo"] == titulo:
                return libro
        return None

    def obtener_lista_libros(self):
        return self.libros


class Autores:
    def __init__(self):
        self.autores_dict = autores_dict

    def agregar_autor(self, nombre_autor, obras):
        self.autores_dict[nombre_autor] = obras

    def consultar_autor(self, autor):
        return self.autores_dict.get(autor, "El autor no se encuentra en la lista.")


class RegistroInteraccion:
    def prestar_libro(self, libro):
        if libro["copias_disponibles"] > 0:
            libro["copias_disponibles"] -= 1
            return True
        else:
            print("No se pudo prestar el libro porque no hay disponibilidad")
            return False

    def devolver_libro(self, libro):
        if libro["copias_disponibles"] < 5:
            libro["copias_disponibles"] += 1
            return True
        else:
            print("No se pudo devolver el libro porque se excedió el límite de copias disponibles")
            return False


class Biblioteca:
    def __init__(self, usuarios):
        self.autores = Autores()
        self.usuarios = usuarios
        self.usuario = None
        self.libros = Libro()
        self.interaccion = RegistroInteraccion()
        self.admin_mode = False

    def mostrar_menu_usuario(self):
        print("Menú de Usuario:")
        print("1. Consultar título")
        print("2. Buscar Autor")
        print("3. Realizar préstamo")
        print("4. Devolver libro")
        print("5. Salir")

    def mostrar_menu_administrador(self):
        print("Menú de Administrador:")
        print("1. Agregar Autor y sus respectivas obras")
        print("2. Mostrar lista de libros")
        print("3. Registrar nuevo usuario")
        print("4. Mostrar Usuarios")
        print("5. Salir")

    def buscar_usuario_por_cuenta(self, cuenta):
        for usuario in self.usuarios:
            if usuario.cuenta == cuenta:
                return usuario
        return None
    
    def mostrar_usuarios(self):
        print("Lista de Usuarios:")
        for usuario in self.usuarios:
            print(f"Nombre: {usuario.nombre}, Cuenta: {usuario.cuenta}, Status: {usuario.status}, Libros Prestados: {usuario.libros_prestados}")

    def ejecutar(self):
        opcion = 0
        while opcion != 6:
            if self.admin_mode:
                self.mostrar_menu_administrador()
            else:
                self.mostrar_menu_usuario()
            opcion = int(input("Seleccione la acción a realizar: "))

            if self.admin_mode:
                if opcion == 1:
                    autor = input("Ingrese el nombre del autor: ")
                    obras = input("Ingrese las obras del autor separadas por comas: ").split(", ")
                    self.autores.agregar_autor(autor, obras)
                elif opcion == 2:
                    lista_libros = self.libros.obtener_lista_libros()
                    for libro in lista_libros:
                        print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Copias disponibles: {libro['copias_disponibles']}")
                elif opcion == 3:
                    nombre = input("Ingrese el nombre del nuevo usuario: ")
                    cuenta = input("Ingrese el número de cuenta del nuevo usuario: ")
                    status = input("Ingrese el estado del nuevo usuario: ")
                    libros_prestados = int(input("Ingrese la cantidad de libros prestados del nuevo usuario: "))  # Cierre de paréntesis corregido
                    nuevo_usuario = Usuario.crear_usuario(nombre, cuenta, status, libros_prestados)
                    self.usuarios.append(nuevo_usuario)
                    print(f"El nuevo usuario {nombre} ha sido registrado.")
                elif opcion == 4:
                    self.mostrar_usuarios()
                elif opcion == 5:
                    self.admin_mode = False
                else:
                    print("Opción no válida.")
            else:  # Modo de usuario
                if opcion == 1:
                    titulo = input("Ingrese el título del libro: ")
                    libro_encontrado = self.libros.obtener_libro_por_titulo(titulo)
                    if libro_encontrado:
                        print(f"Título: {libro_encontrado['titulo']}")
                        print(f"Autor: {libro_encontrado['autor']}")
                        print(f"Género: {libro_encontrado['genero']}")
                        print(f"Copias Disponibles: {libro_encontrado['copias_disponibles']}")
                    else:
                        print("El libro no se encuentra en la biblioteca.")
                elif opcion == 2:
                    autor = input("Ingrese el nombre del autor: ")
                    obras = self.autores.consultar_autor(autor)
                    if obras:
                        print(f"Obras del autor {autor}: {', '.join(obras)}")
                    else:
                        print("El autor no se encuentra en la lista.")
                elif opcion == 3:  # Realizar préstamo
                    cuenta = input("Ingrese su número de cuenta: ")
                    usuario = self.buscar_usuario_por_cuenta(cuenta)
                    if usuario:
                        titulo = input("Ingrese el título del libro a prestar: ")
                        libro = self.libros.obtener_libro_por_titulo(titulo)
                        if libro:
                            if self.interaccion.prestar_libro(libro):
                                usuario.libros_prestados += 1
                                print("El libro ha sido prestado con éxito.")
                            else:
                                print("No se pudo prestar el libro.")
                        else:
                            print("El libro no se encuentra en la biblioteca.")
                    else:
                        print("Usuario no encontrado.")
                elif opcion == 4:  # Devolver libro
                    cuenta = input("Ingrese su número de cuenta: ")
                    usuario = self.buscar_usuario_por_cuenta(cuenta)
                    if usuario:
                        if usuario.libros_prestados > 0:
                            titulo = input("Ingrese el título del libro a devolver: ")
                            libro = self.libros.obtener_libro_por_titulo(titulo)
                            if libro:
                                if self.interaccion.devolver_libro(libro):
                                    usuario.libros_prestados -= 1
                                    print("El libro ha sido devuelto con éxito.")
                                else:
                                    print("No se pudo devolver el libro.")
                            else:
                                print("El libro no se encuentra en la biblioteca.")
                        else:
                            print("El usuario no tiene libros prestados.")
                    else:
                        print("Usuario no encontrado.")
                elif opcion == 5:
                    print("Gracias por visitar la biblioteca.")
                elif opcion == 0:
                    if self.admin_mode:
                        self.admin_mode = False
                    else:
                        self.admin_mode = True
                else:
                    print("Opción no válida.")


if __name__ == "__main__":
    autores_dict = {
        "Friedrich Nietzsche": ["El origen de la tragedia", "Humano demasiado humano"],
        "Herman Hesse": ["Siddhartha", "El lobo estepario"],
        "Simone de Beauvoir": ["La mujer rota", "El segundo sexo"],
        "Platón": ["La República", "Apología de Sócrates"]
    }
    usuarios = [
        Usuario("Jorge", "12345", "Activo", 0),
        Usuario("Yazmin", "23456", "Activo", 1),
        Usuario("Leopoldo", "34567", "Activo", 2)
    ]

    biblioteca = Biblioteca(usuarios)
    biblioteca.ejecutar()
