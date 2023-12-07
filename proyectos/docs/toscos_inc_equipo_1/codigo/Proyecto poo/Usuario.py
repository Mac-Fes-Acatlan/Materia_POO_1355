class Usuario:
    """Los atributos que tendra cualquier usuario base
    """
    def __init__(
        self, nombre: str, apellido: str, fecha: str, correo: str, telefono: str
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if nuevo_nombre is None:
            raise ValueError("Por favor ingresa tu nombre")
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido: str):
        if nuevo_apellido is None:
            raise ValueError("Por favor ingresa tu apellido")
        self._apellido = nuevo_apellido

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, nueva_fecha: str):
        if nueva_fecha is None:
            raise ValueError("Por favor ingresa una fecha")
        self._fecha = nueva_fecha

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo: str):
        if nuevo_correo is None:
            raise ValueError("Por favor ingresa tu correo electronico")
        self._correo = nuevo_correo

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono: str):
        if nuevo_telefono is None:
            raise ValueError("Por favor ingresa tu numero de telefono")
        self._telefono = nuevo_telefono
