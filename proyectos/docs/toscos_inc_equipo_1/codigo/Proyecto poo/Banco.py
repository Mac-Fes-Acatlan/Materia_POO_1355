from pathlib import Path
import pandas as pd
from Cliente import Cliente
from Ejecutivo import Ejecutivo


ruta_ejecutivos = Path(Path.home(), "registro_ejecutivos.csv")
ruta_clientes = Path(Path.home(), "registro_clientes.csv")


class Banco:
    """Banco llevara el registro y todas las operaciones relacionadas
        con los archivos csv
    """
    def generar_csv_clientes():
        ' Comprueba si el archivo de clientes existe'
        if not ruta_clientes.exists():
            #Si no existe, crea un DataFrame con la estructura deseada
            data = {
                "Nombre": [],
                "Apellido": [],
                "Fecha": [],
                "Correo": [],
                "Telefono": [],
                "Contrasenia": [],
                "Numero_Cuenta": [],
                "Saldo": [],
                "Apartado": [],
            }
            df_cliente = pd.DataFrame(data)
            # Guarda el DataFrame en un archivo CSV
            df_cliente.to_csv(ruta_clientes, index=False)
            print("Archivo CSV de clientes creado.")
        else:
            print("El archivo CSV de clientes ya existe.")

    @staticmethod
    def registrar_cliente(usuario: Cliente, df_cliente: pd):
        """Concatena un nuevo cliente en el df

        Args:
            usuario (Cliente)
            df_cliente (pd)

        Returns:
            df_cliente
        """
        new_row = pd.DataFrame(
            {
                "Nombre": [usuario.nombre],
                "Apellido": [usuario.apellido],
                "Fecha": [usuario.fecha],
                "Correo": [usuario.correo],
                "Telefono": [usuario.telefono],
                "Contrasenia": [usuario.contrasenia],
                "Numero_Cuenta": [usuario.numero_cuenta],
                "Saldo": [usuario.saldo],
                "Apartado": [usuario.apartado],
            }
        )
        df_cliente = pd.concat([df_cliente, new_row], ignore_index=True)
        df_cliente.to_csv(ruta_clientes, index=False)
        return df_cliente

    @staticmethod
    def lectura_clientes():
        """Leera y guardara todos los datos del archivo .csv

        Returns:
            dict{Numero_cuenta: objeto cliente}
        """
        df_cliente = pd.read_csv(ruta_clientes)
        personas_diccionario = {}
        for index, row in df_cliente.iterrows():
            usuario = Cliente(
                row["Nombre"],
                row["Apellido"],
                row["Fecha"],
                row["Correo"],
                row["Telefono"],
                row["Contrasenia"],
                row["Numero_Cuenta"],
                float(row["Saldo"]),
                row["Apartado"],
            )
            personas_diccionario[int(row["Numero_Cuenta"])] = usuario
        print(df_cliente)
        print("-" * 100 + "\n")
        return df_cliente, personas_diccionario

    @staticmethod
    def guardar_mov_cliente(usuario: Cliente, df_cliente: pd):
        """Edita los atributos del df segun el cliente

        Args:
            usuario (Cliente): 
            df_cliente (pd): 

        Returns:
            df_cliente: 
        """
        df_cliente.loc[
            df_cliente["Numero_Cuenta"] == usuario.numero_cuenta, "Nombre"
        ] = usuario.nombre
        df_cliente.loc[
            df_cliente["Numero_Cuenta"] == usuario.numero_cuenta, "Apellido"
        ] = usuario.apellido
        df_cliente.loc[
            df_cliente["Numero_Cuenta"] == usuario.numero_cuenta, "Correo"
        ] = usuario.correo
        df_cliente.loc[
            df_cliente["Numero_Cuenta"] == usuario.numero_cuenta, "Telefono"
        ] = usuario.telefono
        df_cliente.loc[
            df_cliente["Numero_Cuenta"] == usuario.numero_cuenta, "Contrasenia"
        ] = usuario.contrasenia
        df_cliente.loc[
            df_cliente["Numero_Cuenta"] == usuario.numero_cuenta, "Saldo"
        ] = usuario.saldo
        df_cliente.loc[
            df_cliente["Numero_Cuenta"] == usuario.numero_cuenta, "Apartado"
        ] = usuario.apartado
        return df_cliente

    @staticmethod
    def eliminar_cliente(numero_cuenta: str, df_ejecutivo: pd):
        """
        Elimina un cliente del DataFrame según su número de cuenta.

        Parameters:
            numero_cuenta (str): Número de cuenta del cliente a eliminar.
            df (pd.DataFrame): DataFrame que contiene la información de los clientes.

        Returns:
            pd.DataFrame: DataFrame actualizado sin el cliente eliminado.
        """
        df_ejecutivo = df_ejecutivo[df_ejecutivo["Numero_Cuenta"] != numero_cuenta]
        df_ejecutivo.to_csv(ruta_clientes, index=False)
        return df_ejecutivo

    def generar_csv_ejecutivos():
        'Comprueba si el archivo de ejecutivos existe'
        if not ruta_ejecutivos.exists():
            # Si no existe, crea un DataFrame con la estructura deseada
            data = {
                "Nombre": [],
                "Apellido": [],
                "Fecha": [],
                "Correo": [],
                "Telefono": [],
                "Contrasenia": [],
                "Numero_Cuenta": [],
                "Puesto": [],
                "Sucursal": [],
            }
            df_ejecutivo = pd.DataFrame(data)
            # Guarda el DataFrame en un archivo CSV
            df_ejecutivo.to_csv(ruta_ejecutivos, index=False)
            print("Archivo CSV de ejecutivos creado.")
        else:
            print("El archivo CSV de ejecutivos ya existe.")

    @staticmethod
    def registrar_ejecutivo(usuario: Ejecutivo, df_ejecutivo: pd):
        """Concatena un nuevo ejecutivo en el df

        Args:
            usuario (Ejecutivo)
            df_ejecutivo (pd)

        Returns:
            df_ejecutivo
        """
        new_row = pd.DataFrame(
            {
                "Nombre": [usuario.nombre],
                "Apellido": [usuario.apellido],
                "Fecha": [usuario.fecha],
                "Correo": [usuario.correo],
                "Telefono": [usuario.telefono],
                "Contrasenia": [usuario.contrasenia],
                "Numero_Cuenta": [usuario.numero_cuenta],
                "Puesto": [usuario.puesto],
                "Sucursal": [usuario.sucursal],
            }
        )
        df_ejecutivo = pd.concat([df_ejecutivo, new_row], ignore_index=True)
        df_ejecutivo.to_csv(ruta_ejecutivos, index=False)
        return df_ejecutivo

    @staticmethod
    def lectura_ejecutivos():
        """Leera y guardara todos los datos del archivo .csv

        Returns:
            dict{Numero_cuenta: objeto ejecutivo}
        """
        df_ejecutivo = pd.read_csv(ruta_ejecutivos)
        personas_diccionario = {}
        for index, row in df_ejecutivo.iterrows():
            usuario = Ejecutivo(
                row["Nombre"],
                row["Apellido"],
                row["Fecha"],
                row["Correo"],
                row["Telefono"],
                row["Contrasenia"],
                row["Numero_Cuenta"],
                row["Puesto"],
                row["Sucursal"],
            )
            personas_diccionario[(row["Numero_Cuenta"])] = usuario
        print(df_ejecutivo)
        print("-" * 115 + "\n")
        return df_ejecutivo, personas_diccionario

    @staticmethod
    def guardar_mov_ejecutivos(usuario: Ejecutivo, df_ejecutivo: pd):
        """Edita los atributos del df segun el ejecutivo

        Args:
            usuario (Ejecutivo): 
            df_ejecutivo (pd): 

        Returns:
            df_ejecutivo: 
        """
        df_ejecutivo.loc[
            df_ejecutivo["Numero_Cuenta"] == usuario.numero_cuenta, "Nombre"
        ] = usuario.nombre
        df_ejecutivo.loc[
            df_ejecutivo["Numero_Cuenta"] == usuario.numero_cuenta, "Apellido"
        ] = usuario.apellido
        df_ejecutivo.loc[
            df_ejecutivo["Numero_Cuenta"] == usuario.numero_cuenta, "Correo"
        ] = usuario.correo
        df_ejecutivo.loc[
            df_ejecutivo["Numero_Cuenta"] == usuario.numero_cuenta, "Telefono"
        ] = usuario.telefono
        df_ejecutivo.loc[
            df_ejecutivo["Numero_Cuenta"] == usuario.numero_cuenta, "Contrasenia"
        ] = usuario.contrasenia
        df_ejecutivo.loc[
            df_ejecutivo["Numero_Cuenta"] == usuario.numero_cuenta, "Puesto"
        ] = usuario.puesto
        df_ejecutivo.loc[
            df_ejecutivo["Numero_Cuenta"] == usuario.numero_cuenta, "Sucursal"
        ] = usuario.sucursal
        return df_ejecutivo

    @staticmethod
    def guardar_clientes(df_clientes: pd):
        """Guarda el nuevo df en la ruta 

        Args:
            df_clientes (pd):
        """
        df_clientes.to_csv(ruta_clientes, index=False)

    @staticmethod
    def guardar_ejecutivos(df_ejecutivos):
        """Guarda el nuevo df en la ruta

        Args:
            df_ejecutivos (_type_): 
        """
        df_ejecutivos.to_csv(ruta_ejecutivos, index=False)


Banco.generar_csv_clientes()
Banco.generar_csv_ejecutivos()
df_cliente_global, diccionario_clientes = Banco.lectura_clientes()
df_ejecutivo_global, diccionario_ejecutivos = Banco.lectura_ejecutivos()
