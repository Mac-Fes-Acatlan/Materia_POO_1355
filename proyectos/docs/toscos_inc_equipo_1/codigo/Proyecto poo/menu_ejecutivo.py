import datetime
from Banco import *



class MenuEjecutivo:
    """Todos los metodos a los que solo un ejecutivo tendra acceso
    """
    def __init__(self, usuario: Ejecutivo) -> None:
        self.usuario = usuario

    def menu(self):
        global df_cliente_global
        global df_ejecutivo_global
        global diccionario_clientes
        global diccionario_ejecutivos
        print(f"Bienvenido {self.usuario.nombre}\n")
        while True:
            print("----Estas son las opciones----")
            print("1. Registrar clientes")
            print("2. Modificar datos personales")
            print("3. Ver registro clientes")
            print("4. Registrar ejecutivo")
            print("5. Consultar saldo de cliente")
            print("6. Eliminar cliente")
            print("7. Congelar cuenta del cliente")
            print("8. Salir del menu..")
            try:
                opcion = int(input("Ingrese una opcion: "))
                [1, 2, 3, 4, 5, 6, 7, 8].index(opcion)
            except ValueError:
                print("Esa no es una opcion valida.")

            if opcion == 1:
                print("\n")
                df_cliente_global = self.registrar_cliente_nuevo(df_cliente_global)
                df_cliente_global, diccionario_clientes = Banco.lectura_clientes()
            elif opcion == 2:
                print("\n")
                df_cliente_global = self.modificar_datos_cliente(df_cliente_global)
            elif opcion == 3:
                print("\n")
                print(df_cliente_global)
                print("-" * 110)
            elif opcion == 4:
                print("\n")
                df_ejecutivo_global = self.registrar_ejecutivo_nuevo(
                    df_ejecutivo_global
                )
                df_ejecutivo_global, diccionario_ejecutivos = Banco.lectura_ejecutivos()
            elif opcion == 5:
                print("\n")
                self.consultar_saldo_cliente()
            elif opcion == 6:
                print("\n")
                df_cliente_global = self.eliminar_cliente(df_cliente_global)
                df_cliente_global, diccionario_clientes = Banco.lectura_clientes()
            elif opcion == 7:
                print("\n")
                self.congelar_cliente()
            else:
                print("\n")
                print("Saliendo del menú...")
                break
            Banco.guardar_clientes(df_cliente_global)
            Banco.guardar_ejecutivos(df_ejecutivo_global)

    def registrar_cliente_nuevo(self, df_cliente):
        """Ingresa los valores para un nuevo ejecutivo
            lo crea y lo almacena en el df

        Args:
            df_cliente 

        Returns:
            df_cliente: 
        """
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        fecha = str(datetime.date.today())
        correo = input("Correo: ")
        telefono = input("Telefono: ")
        contrasenia = input("Contraseña: ")
        numero_cuenta = input("Numero de cuenta: ")
        saldo = 0
        apartado = 0
        cliente_nuevo = Cliente(
            nombre,
            apellido,
            fecha,
            correo,
            telefono,
            contrasenia,
            numero_cuenta,
            saldo,
            apartado,
        )
        df_cliente = Banco.registrar_cliente(cliente_nuevo, df_cliente)
        return df_cliente

    @classmethod
    def registrar_ejecutivo_nuevo(cls, df_ejecutivo):
        """Ingresa los valores para un nuevo ejecutivo
            lo crea y lo almacena en el df

        Args:
            df_ejecutivo

        Returns:
            df_ejecutivo
        """
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        fecha = str(datetime.date.today())
        correo = input("Correo: ")
        telefono = input("Telefono: ")
        contrasenia = input("Contraseña: ")
        numero_cuenta = input("Numero de cuenta: ")
        puesto = input("Puesto: ")
        sucursal = input("Sucursal: ")
        ejecutivo_nuevo = Ejecutivo(
            nombre,
            apellido,
            fecha,
            correo,
            telefono,
            contrasenia,
            numero_cuenta,
            puesto,
            sucursal,
        )
        df_ejecutivo = Banco.registrar_ejecutivo(ejecutivo_nuevo, df_ejecutivo)
        return df_ejecutivo

    def modificar_datos_cliente(self, df_cliente):
        """Modifica un cliente desde el diccionario y modifica el df

        Args:
            df_cliente (_type_): 

        Returns:
            df_cliente: modificado
        """
        global diccionario_clientes
        cuenta = int(input("Ingrese el numero de cuenta: "))
        if cuenta in diccionario_clientes.keys():
            cliente = diccionario_clientes[cuenta]
            print(cliente.nombre)
            print("Campos disponibles para modificar:")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Fecha de nacimiento")
            print("4. Correo electrónico")
            print("5. Teléfono")
            print("6. Contraseña")

            opcion = input("Seleccione el número del campo que desea modificar (1-6): ")

            if opcion == "1":
                nuevo_valor = input("Ingrese el nuevo nombre: ")
                cliente.nombre = nuevo_valor
            elif opcion == "2":
                nuevo_valor = input("Ingrese el nuevo apellido: ")
                cliente.apellido = nuevo_valor
            elif opcion == "3":
                nuevo_valor = input(
                    "Ingrese la nueva fecha de nacimiento (AAAA-MM-DD): "
                )
                cliente.fecha = nuevo_valor
            elif opcion == "4":
                nuevo_valor = input("Ingrese el nuevo correo electrónico: ")
                cliente.correo = nuevo_valor
            elif opcion == "5":
                nuevo_valor = input("Ingrese el nuevo número de teléfono: ")
                cliente.telefono = nuevo_valor
            elif opcion == "6":
                nuevo_valor = input("Ingrese la nueva contraseña: ")
                cliente.contrasenia = nuevo_valor
            else:
                print("Opción no válida. No se realizó ninguna modificación.")

            # Guardar los cambios en el archivo CSV
            df_cliente = Banco.guardar_mov_cliente(cliente, df_cliente)
            return df_cliente

        print(f"No se encontró ningún cliente con el número de cuenta {cuenta}.")

    def consultar_saldo_cliente(self):
        """Busca un usuario en los diccionarios y muestra su saldo
        """
        cuenta = int(input("Ingrese el numero de cuenta: "))
        if cuenta in diccionario_clientes.keys():
            cliente = diccionario_clientes[cuenta]
            print(
                f"Cliente {cliente.nombre} {cliente.apellido} con saldo: {cliente.saldo}\n"
            )
        else:
            print(f"No se encontró ningún cliente con el número de cuenta {cuenta}.")

    def eliminar_cliente(self, df_cliente):
        """Elimina un renglon del df

        Args:
            df_cliente

        Returns:
            df_cliente: con un renglon menos
        """
        cuenta = int(input("Ingrese el numero de cuenta: "))
        if cuenta in diccionario_clientes.keys():
            df_cliente = Banco.eliminar_cliente(cuenta, df_cliente)
            return df_cliente
        print(f"No se encontró ningún cliente con el número de cuenta {cuenta}.")
