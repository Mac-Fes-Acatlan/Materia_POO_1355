from Ejecutivo import CrearCuenta


class Cliente(CrearCuenta):
    """Clase final del comportamiento de un cliente

    Args:
        CrearCuenta: Nos hereda todos los atributos de una cuenta general
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
        saldo: float,
        apartado: float,
    ):
        super().__init__(
            nombre, apellido, fecha, correo, telefono, contrasenia, numero_cuenta
        )
        self.saldo = saldo
        self.apartado = apartado

