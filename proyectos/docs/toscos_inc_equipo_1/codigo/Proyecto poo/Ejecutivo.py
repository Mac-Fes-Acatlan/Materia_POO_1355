import random
from Usuario import Usuario



class CrearCuenta(Usuario):
    """Clase madre de los 2 tipos de usuario

    Args:
        Usuario : Nos hereda los atributos de una perosna
    """
    def __init__(
        self,
        nombre: str,
        apellido: str,
        fecha: str,
        correo: str,
        telefono: str,
        contrasenia: str,
        numero_cuenta,
    ):
        super().__init__(nombre, apellido, fecha, correo, telefono)
        self.contrasenia = contrasenia
        self.numero_cuenta = numero_cuenta or self.asignar_numero_cuenta()

    def generar_contrasenia(self, contrasenia: str):
        """Generador de contraseña

        Args:
            contrasenia (str)
        """
        print("Tu contraseña es: ", contrasenia)

    def asignar_numero_cuenta(self):
        """Genera el numero de cuenta con tamaño especifico

        Returns:
            numero de cuenta
        """
        self.numero_cuenta = random.randint(100000, 999999)
        print(f"Número de cuenta asignado: {self.numero_cuenta}")
        return int(self.numero_cuenta)


class Ejecutivo(
    CrearCuenta
):
    """Clase final que define el comportamiento ddel usuario

    Args:
        CrearCuenta : Le hereda todos los atributos
    """
    def __init__(
        self,
        nombre: str,
        apellido: str,
        fecha: str,
        correo: str,
        telefono: str,
        contrasenia: str,
        numero_cuenta,
        puesto: str,
        sucursal: str,
    ):
        super().__init__(
            nombre, apellido, fecha, correo, telefono, contrasenia, numero_cuenta
        )
        self.puesto = puesto
        self.sucursal = sucursal

    @property
    def puesto(self):
        return self._puesto

    @puesto.setter
    def puesto(self, nuevo_puesto: str):
        if nuevo_puesto is None:
            raise ValueError("No ha ingresado el nuevo puesto")
        self._puesto = nuevo_puesto

    @property
    def sucursal(self):
        return self._sucursal

    @sucursal.setter
    def sucursal(self, nueva_sucursal: str):
        if nueva_sucursal is None:
            raise ValueError("No has ingresado la nueva sucursal")
        self._sucursal = nueva_sucursal
