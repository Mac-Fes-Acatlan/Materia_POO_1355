import pandas as pd
from datetime import datetime


class Libro:
    def __init__(self, codigo, titulo, autor, localizacion, genero, disponible):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._localizacion = localizacion
        self._genero = genero
        self._disponible = disponible

    # Codigo
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, new_codigo):
        self._codigo = new_codigo

    # Titulo
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, new_titulo):
        self._titulo = new_titulo

    # Autor
    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, new_autor):
        self._autor = new_autor

    # Localizacion
    @property
    def localizacion(self):
        return self._localizacion

    @localizacion.setter
    def localizacion(self, new_localizacion):
        self._localizacion = new_localizacion

    # Genero
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, new_genero):
        self._genero = new_genero

    # Disponibilidad
    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, new_disponible):
        self._disponible = new_disponible


class Usuario:
    def __init__(self, numero, nombre, direccion):
        self._numero = numero
        self._nombre = nombre
        self._direccion = direccion

    # Numero
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, new_numero):
        self._numero = new_numero

    # Nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre

    # Direccion
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, new_direccion):
        self._direccion = new_direccion


class Prestamo:
    def __init__(self, codigoLibro, numeroUsuario, fecha):
        self._codigoLibro = codigoLibro
        self._numeroUsuario = numeroUsuario
        self._fecha = fecha

    # Codigo
    @property
    def codigoLibro(self):
        return self._codigoLibro

    @codigoLibro.setter
    def codigoLibro(self, new_codigoLibro):
        self._codigoLibro = new_codigoLibro

    # Numero
    @property
    def numeroUsuario(self):
        return self._numeroUsuario

    @numeroUsuario.setter
    def numeroUsuario(self, new_numeroUsuario):
        self._numeroUsuario = new_numeroUsuario

    # Fecha
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, new_fecha):
        self._fecha = new_fecha


def obtener_libros():
    try:
        libros_df = pd.read_csv(
            "libros.txt",
            sep=";",
            names=["codigo", "titulo", "autor", "localizacion", "genero", "disponible"],
        )
        libros = [Libro(**row) for _, row in libros_df.iterrows()]
        return libros
    except FileNotFoundError:
        return []


def registrar_libro(libro):
    libros = obtener_libros()
    libros.append(libro)
    libros_df = pd.DataFrame(
        [
            {
                "codigo": libro.codigo,
                "titulo": libro.titulo,
                "autor": libro.autor,
                "localizacion": libro.localizacion,
                "genero": libro.genero,
                "disponible": libro.disponible,
            }
            for libro in libros
        ]
    )
    libros_df.to_csv("libros.txt", sep=";", index=False, header=False)


def obtener_usuarios():
    try:
        usuarios_df = pd.read_csv(
            "usuarios.txt", sep=";", names=["numero", "nombre", "direccion"]
        )
        usuarios = [Usuario(**row) for _, row in usuarios_df.iterrows()]
        return usuarios
    except FileNotFoundError:
        return []


def registrar_usuario(usuario):
    usuarios = obtener_usuarios()
    usuarios.append(usuario)
    usuarios_df = pd.DataFrame(
        [
            {
                "numero": usuario.numero,
                "nombre": usuario.nombre,
                "direccion": usuario.direccion,
            }
            for usuario in usuarios
        ]
    )
    usuarios_df.to_csv("usuarios.txt", sep=";", index=False, header=False)


def obtener_prestamos():
    try:
        prestamos_df = pd.read_csv(
            "prestamos.txt", sep=";", names=["codigoLibro", "numeroUsuario", "fecha"]
        )
        prestamos = [
            Prestamo(
                row["codigoLibro"],
                row["numeroUsuario"],
                datetime.strptime(row["fecha"], "%Y-%m-%d %H:%M:%S"),
            )
            for _, row in prestamos_df.iterrows()
        ]
        return prestamos
    except FileNotFoundError:
        return []


def registrar_prestamo(prestamo):
    prestamos = obtener_prestamos()
    prestamos.append(prestamo)
    prestamos_df = pd.DataFrame(
        [
            {
                "codigoLibro": prestamo.codigoLibro,
                "numeroUsuario": prestamo.numeroUsuario,
                "fecha": prestamo.fecha.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for prestamo in prestamos
        ]
    )
    prestamos_df.to_csv("prestamos.txt", sep=";", index=False, header=False)
    marcar_libro_como_prestado(prestamo.codigoLibro)


def marcar_libro_como_prestado(codigo_libro):
    libros = obtener_libros()
    for libro in libros:
        if libro.codigo == codigo_libro:
            libro.disponible = False
    libros_df = pd.DataFrame(
        [
            {
                "codigo": libro.codigo,
                "titulo": libro.titulo,
                "autor": libro.autor,
                "localizacion": libro.localizacion,
                "genero": libro.genero,
                "disponible": libro.disponible,
            }
            for libro in libros
        ]
    )
    libros_df.to_csv("libros.txt", sep=";", index=False, header=False)


while True:
    print("1. Registrar usuario")
    print("2. Registrar libro")
    print("3. Registrar prestamo")
    print("4. Ver usuarios")
    print("5. Ver libros disponibles")
    print("6. Ver prestamos")
    print("7. Salir")

    eleccion = input("Elige: ")

    if eleccion == "1":
        numero = input("Ingrese numero de usuario: ")
        nombre = input("Ingrese nombre de usuario: ")
        direccion = input("Ingrese direccion de usuario: ")
        registrar_usuario(Usuario(numero, nombre, direccion))
        print("Usuario registrado exitosamente")

    elif eleccion == "2":
        codigo = input("Ingrese el codigo del libro: ")
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        disponible = input("El libro esta disponible? [true/false]: ")
        localizacion = input("Ingrese la localizacion del libro: ")
        genero = input("Ingrese el genero del libro: ")
        registrar_libro(
            Libro(
                codigo,
                titulo,
                autor,
                localizacion,
                genero,
                disponible.lower() == "true",
            )
        )
        print("Libro registrado correctamente")

    elif eleccion == "3":
        codigo_libro = input("Ingrese el codigo del libro: ")
        numero_usuario = input("Ingrese el numero de usuario: ")
        registrar_prestamo(Prestamo(codigo_libro, numero_usuario, datetime.now()))
        marcar_libro_como_prestado(codigo_libro)
        print("Prestamo registrado correctamente")

    elif eleccion == "4":
        usuarios = obtener_usuarios()
        usuarios_df = pd.DataFrame(
            [
                {
                    "numero": usuario.numero,
                    "nombre": usuario.nombre,
                    "direccion": usuario.direccion,
                }
                for usuario in usuarios
            ]
        )
        print(usuarios_df)

    elif eleccion == "5":
        libros = obtener_libros()
        libros_disponibles = [libro for libro in libros if libro.disponible]
        libros_df = pd.DataFrame(
            [
                {
                    "codigo": libro.codigo,
                    "titulo": libro.titulo,
                    "autor": libro.autor,
                    "localizacion": libro.localizacion,
                    "genero": libro.genero,
                    "disponible": libro.disponible,
                }
                for libro in libros_disponibles
            ]
        )
        print(libros_df)

    elif eleccion == "6":
        prestamos = obtener_prestamos()
        prestamos_df = pd.DataFrame(
            [
                {
                    "codigoLibro": prestamo.codigoLibro,
                    "numeroUsuario": prestamo.numeroUsuario,
                    "fecha": prestamo.fecha.strftime("%Y-%m-%d %H:%M:%S"),
                }
                for prestamo in prestamos
            ]
        )
        print(prestamos_df)

    elif eleccion == "7":
        break
