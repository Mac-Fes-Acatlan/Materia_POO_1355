"""Clase PersonaCliente"""
from Persona import Persona

class PersonaCliente(Persona):
    """
    Clase que hereda de Persona y guarda información de clientes.
    """

    def __init__(self,
                 nombre: str,
                 usuario: str,
                 password: str,
                 direccion: str,
                 telefono: str,
                 email: str,
                 tarjeta: str
                 ):
        super().__init__(nombre, usuario, password, direccion, telefono)
        self.email = email
        self.tarjeta = tarjeta

    @property
    def email(self):
        """get email"""
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def tarjeta(self):
        """ get tarjeta"""
        return self._tarjeta

    @tarjeta.setter
    def tarjeta(self, new_tarjeta):
        self._tarjeta = new_tarjeta
