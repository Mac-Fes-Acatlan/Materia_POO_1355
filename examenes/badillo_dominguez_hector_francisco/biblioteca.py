import os
import random


class Libro:
    def __init__(self, titulo: str, autor: str, status: bool) -> None:
        self._titulo = titulo
        self._autor = autor
        self._status = status

    def mostrar_libro(self):
        estado = "Disponible" if self.status else "Prestado"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Estado: {estado}")
        print("=" * 30)

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        self._titulo = nuevo_titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor: str):
        self._autor = nuevo_autor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, nuevo_status: bool):
        self._status = nuevo_status


class CatalogoLibros:
    def __init__(self) -> None:
        self.libros = []

    def agregar_libro(self, titulo: str, autor: str):
        nuevo_libro = Libro(titulo, autor, True)
        self.libros.append(nuevo_libro)

    def editar_status(self, titulo: str, nuevo_status: bool):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.status != nuevo_status:
                    libro.status = nuevo_status
                    return True
        return False

    def eliminar_libro(self, titulo: str):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                return True
        return False

    def libros_por_defecto(self):
        """Libros que estaran el el catalogo por defecto"""
        self.agregar_libro("El gran Gatsby", "F. Scott Fitzgerald")
        self.agregar_libro("Cien años de soledad", "Gabriel Garcia Marquez")
        self.agregar_libro("1984", "George Orwell")

    def mostrar_catalogo(self):
        for libro in self.libros:
            estado = "Disponible" if libro.status else "Prestado"
            print(f"Título: {libro.titulo}")
            print(f"Autor: {libro.autor}")
            print(f"Estado: {estado}")
            print("=" * 30)


class UsuarioCliente:
    def __init__(self, nombre: str, usuario: str, password: str, telefono: int) -> None:
        self._nombre = nombre
        self._usuario = usuario
        self._password = password
        self._telefono = telefono

    def buscar_libro(self, catalogo: CatalogoLibros, titulo: str):
        for libro in catalogo.libros:
            if libro.titulo == titulo:
                print(libro.mostrar_libro())
                return True
        print("Libro no encontrado.")
        return False

    def prestamo_libro(self, catalogo: CatalogoLibros, titulo: str):
        if catalogo.editar_status(titulo, False):
            print("Libro prestado")
            numero_transaccion = "".join([str(random.randint(0, 9)) for _ in range(13)])
            print(f"Con este numero pida libro en caja: {numero_transaccion}")
        else:
            print("No se puede prestar el libro.")

    def devolver_libro(self, catalogo: CatalogoLibros, titulo: str):
        if self.buscar_libro(catalogo, titulo):
            if catalogo.editar_status(titulo, True):
                print("Libro devuelto")
                numero_transaccion = "".join(
                    [str(random.randint(0, 9)) for _ in range(13)]
                )
                print(f"Con este numero devuelva libro en caja: {numero_transaccion}")
            else:
                print("No se puede devolver el libro")

    def mostrar_libros(self, catalogo: CatalogoLibros):
        catalogo.mostrar_catalogo()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, nuevo_usuario):
        self._usuario = nuevo_usuario

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, nueva_password):
        self._password = nueva_password

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self._telefono = nuevo_telefono


class UsuarioAdministrador:
    def __init__(
        self, nombre: str, usuario: str, password: str, id_empleado: int
    ) -> None:
        self._nombre = nombre
        self._usuario = usuario
        self._password = password
        self._id_empleado = id_empleado

    def agregar_libro(self, catalogo: CatalogoLibros):
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        libro_nuevo = Libro(titulo, autor, True)
        catalogo.libros.append(libro_nuevo)

    def eliminar_libro(self, catalogo: CatalogoLibros, titulo: str):
        if catalogo.eliminar_libro(titulo):
            print("Libro Eliminado")
        else:
            print("Libro no encontrado")

    def mostrar_libros(self, catalogo: CatalogoLibros):
        catalogo.mostrar_catalogo()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, nuevo_usuario):
        self._usuario = nuevo_usuario

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, nueva_password):
        self._password = nueva_password

    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, nuevo_id_empleado):
        self._id_empleado = nuevo_id_empleado


class IniciarSesion:
    def __init__(self) -> None:
        self._cliente = UsuarioCliente("Hector Badillo", "Hector", "Examen", 5534018632)
        self._administrador = UsuarioAdministrador(
            "Hector Badillo", "Administrador", "Examen", 92759
        )

    def entrar(self):
        usuario = None
        while not isinstance(usuario, (UsuarioAdministrador, UsuarioCliente)):
            nombre = input("Ingrese Usuario: ")
            password = input("Ingrese Contraseña: ")
            usuario = self.validacion(nombre, password)
        return usuario

    def validacion(self, usuario: str, password: str):
        if (usuario == self._cliente.usuario) and (password == self._cliente.password):
            return self._cliente
        if (usuario == self._administrador.usuario) and (
            password == self._administrador.password
        ):
            return self._administrador
        
        print("Usuario no encontrado")
        return False

    def sesion_administrador(self, catalogo:CatalogoLibros, usuario: UsuarioAdministrador):
        os.system("cls")
        print(f"Sesion iniciada como administrador {usuario.nombre}")

        opcion = None
        while opcion not in range(1, 5):
            print("\n\tMENU")
            print("1.Mostrar catalogo")
            print("2.Añadir libro")
            print("3.Eliminar libro")
            print("4.Salir")
            opcion = input("Introduzca el numero de su opcion: ")
            match opcion:
                case "1":
                    print("\nMostrar catalogo")
                    print("=" * 30)
                    usuario.mostrar_libros(catalogo)
                case "2":
                    print("\nAgregar libro")
                    print("=" * 30)
                    usuario.agregar_libro(catalogo)
                case "3":
                    print("\nEliminar libro")
                    print("=" * 30)
                    titulo_elimiar = input("Titulo del libro que desea eliminar: ")
                    usuario.eliminar_libro(catalogo, titulo_elimiar)
                case "4":
                    break

    def sesion_cliente(self, catalogo:CatalogoLibros, usuario: UsuarioCliente):
        os.system("cls")
        print(f"Sesion iniciada como cliente {usuario.nombre}")

        opcion = None
        while opcion not in range(1, 5):
            print("\n\tMENU")
            print("1.Buscar libro")
            print("2.Mostrar catalogo")
            print("3.Devolver libro")
            print("4.Salir")
            opcion = input("Introduzca el numero de su opcion: ")
            match opcion:
                case "1":
                    opc = 1

                    while opc == 1:
                        print("\nBusqueda de libro")
                        print("=" * 30)
                        titulo = input("Titulo: ")
                        print("=" * 30)
                        usuario.buscar_libro(catalogo, titulo)
                        print("Pedir prestamo")
                        print("1. Si")
                        print("2. No")
                        prestamo = int(input("Opcion: "))
                        if prestamo == 1:
                            print("=" * 30)
                            print("\nPrestamo de libro")
                            usuario.prestamo_libro(catalogo, titulo)
                            print("=" * 30)
                        print("\nBuscar otro libro")
                        print("1. Si")
                        print("2. No")
                        opc = int(input("Opcion: "))

                case "2":
                    print("\nMostrar catalogo")
                    print("=" * 30)
                    usuario.mostrar_libros(catalogo)
                case "3":
                    print("=" * 30)
                    print("\nDevolver libro")
                    print("=" * 30)
                    titulo = input("Titulo: ")
                    usuario.devolver_libro(catalogo, titulo)
                case "4":
                    break


catalogo_iniciado = CatalogoLibros()
catalogo_iniciado.libros_por_defecto()

REGISTRO = 2
while REGISTRO == 2:
    sesion = IniciarSesion()
    usuario_iniciado = sesion.entrar()

    if isinstance(usuario_iniciado, UsuarioAdministrador):
        sesion.sesion_administrador(catalogo_iniciado, usuario_iniciado)

    if isinstance(usuario_iniciado, UsuarioCliente):
        sesion.sesion_cliente(catalogo_iniciado, usuario_iniciado)

    os.system("cls")
    print("Cerrar sistema")
    print("1. Si")
    print("2. No")
    REGISTRO = int(input("Opcion: "))
    os.system("cls")
