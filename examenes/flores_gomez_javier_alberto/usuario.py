from libro import Libro


class Usuario:
    def __init__(self, nombre_usuario: str, password: str, codigo: int):
        self._nombre_usuario = nombre_usuario
        self._password = password
        self._codigo_usuario = codigo
        self._libros_prestados = []
        self._libros_reservados = Libro
        self._reserva = False

    @property
    def nombre_usuario(self):
        return self._nombre_usuario

    @property
    def password(self):
        return self._password

    @property
    def codigo_usuario(self):
        return self._codigo_usuario

    @property
    def libros_prestados(self):
        return self._libros_prestados

    @property
    def libros_reservados(self):
        return self._libros_reservados

    @property
    def reserva(self):
        return self._reserva

    @nombre_usuario.setter
    def nombre_usuario(self, nombre):
        self._nombre_usuario = nombre

    @password.setter
    def password(self, password):
        self._password = password

    @codigo_usuario.setter
    def codigo_usuario(self, codigo):
        self._codigo_usuario = codigo

    @libros_reservados.setter
    def libros_reservados(self, libro):
        self._libros_reservados = libro

    @reserva.setter
    def reserva(self, reserva):
        self._reserva = reserva
