from Banco import *


class MenuCliente:
    """Menu al que solo los clientes tendran acceso
    """
    def __init__(self, usuario: Cliente):
        self.usuario = usuario

    def menucliente(self):
        """Menu

        Raises:
            ValueError: Para que el usuario no ingrese opciones invalidas
        """
        global df_cliente_global
        print(f"Hola de vuelta, {self.usuario.nombre}")
        while True:
            print("\n----Bienvenido, elige una opcion para comenzar----")
            print("1. Consultar Saldo.")
            print("2. Apartar dinero.")
            print("3. Transferir.")
            print("4. Consultar datos personales.")
            print("5. Modificar Datos.")
            print("6. Depositar")
            print("7.Retirar")
            print("8. Salir.")
            try:
                opcion = int(input("Ingrese la acción a realizar: "))
                if opcion not in [1, 2, 3, 4, 5, 6, 7, 8]:
                    raise ValueError
            except ValueError:
                print("Esa no es una opción válida.")
                continue

            if opcion == 1:
                self.consultar_saldo()
            elif opcion == 2:
                self.apartar_dinero()
            elif opcion == 3:
                self.transferir()
            elif opcion == 4:
                self.consultar_datos()
            elif opcion == 5:
                self.modificar_datos_cliente()
            elif opcion == 6:
                self.depositar_dinero()
            elif opcion == 7:
                self.retirar_dinero()
            elif opcion == 8:
                print("\nSaliendo del menú...")
                Banco.guardar_clientes(df_cliente_global)

                break

    def consultar_saldo(self):
        print(f"Su saldo actual es: {self.usuario.saldo}")

    def apartar_dinero(self):
        global df_cliente_global
        try:
            cantidad = float(input("Ingrese la cantidad a apartar: "))
            if cantidad <= 0 or cantidad > self.usuario.saldo:
                raise ValueError("Cantidad inválida.")
            self.usuario.saldo -= cantidad
            self.usuario.apartado += cantidad
            print(
                f"Se han apartado {cantidad} con éxito. Saldo actual: {self.usuario.saldo}"
            )
            df_cliente_global = Banco.guardar_mov_cliente(
                self.usuario, df_cliente_global
            )

        except ValueError as e:
            print(e)

    def transferir(self):
        global df_cliente_global
        try:
            cuenta_destino = int(input("Ingrese el número de cuenta destino: "))
            cantidad = float(input("Ingrese la cantidad a transferir: "))
            if cantidad <= 0 or cantidad > self.usuario.saldo:
                raise ValueError("Cantidad inválida.")

            cliente_destino = diccionario_clientes[cuenta_destino]
            if cliente_destino is None:
                raise ValueError("La cuenta destino no existe.")

            self.usuario.saldo -= cantidad
            cliente_destino.saldo += cantidad
            print(
                f"Transferencia exitosa de {cantidad} a la cuenta {cuenta_destino}. Saldo actual: {self.usuario.saldo}"
            )

            # Actualizar los datos en los CSV
            df_cliente_global = Banco.guardar_mov_cliente(
                self.usuario, df_cliente_global
            )
            df_cliente_global = Banco.guardar_mov_cliente(
                cliente_destino, df_cliente_global
            )

        except ValueError as e:
            print(e)

    def consultar_datos(self):
        print(f"Nombre: {self.usuario.nombre}")
        print(f"Apellido: {self.usuario.apellido}")
        print(f"Correo: {self.usuario.correo}")
        print(f"Telefono: {self.usuario.telefono}")

    def modificar_datos_cliente(self):
        global df_cliente_global
        print(f"Modificando datos de: {self.usuario.nombre}")
        print("Campos disponibles para modificar:")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Correo electrónico")
        print("4. Teléfono")
        print("5. Contraseña")

        try:
            opcion = int(
                input("Seleccione el número del campo que desea modificar (1-5): ")
            )
            if opcion not in [1, 2, 3, 4, 5]:
                raise ValueError

            nuevo_valor = input("Ingrese el nuevo valor: ")
            if opcion == 1:
                self.usuario.nombre = nuevo_valor
            elif opcion == 2:
                self.usuario.apellido = nuevo_valor
            elif opcion == 3:
                self.usuario.correo = nuevo_valor
            elif opcion == 4:
                self.usuario.telefono = nuevo_valor
            elif opcion == 5:
                self.usuario.contrasenia = nuevo_valor

            df_cliente_global = Banco.guardar_mov_cliente(
                self.usuario, df_cliente_global
            )

        except ValueError:
            print("Opción no válida. No se realizó ninguna modificación.")

    def depositar_dinero(self):
        global df_cliente_global
        deposito = float(input("Ingrese la cantidad a depositar: "))
        self.usuario.saldo += deposito
        df_cliente_global = Banco.guardar_mov_cliente(self.usuario, df_cliente_global)

    def retirar_dinero(self):
        global df_cliente_global
        retiro = float(input("Ingrese la cantidad a retirar: "))
        self.usuario.saldo -= retiro
        df_cliente_global = Banco.guardar_mov_cliente(self.usuario, df_cliente_global)
