from menu_ejecutivo import *
from menu_cliente import *


class Login:
    """Leera el tipo de usuario ingresado e iniciara sesion
    """
    def iniciar_sesion(self):
        """Solo pedira al usuario si tiene cuenta o no 
        """
        global df_cliente_global
        global diccionario_clientes
        print("Bienvenido al Banco Salgado")
        while True:
            status_cuenta = int(
                input("¿Tiene una cuenta con nosotros? \n 1 (sí) 2 (no) \n")
            )
            if status_cuenta == 1:
                self.iniciar_sesion_usuario()
                break
            elif status_cuenta == 2:
                self.registrar_cliente()
                df_cliente_global, diccionario_clientes = Banco.lectura_clientes()
                break
            else:
                print("Ha seleccionado una opción no válida")

    def iniciar_sesion_usuario(self):
        """Revisara la informacion ingresaada e iniciara sesion,
            mandara al menu correspondiente
        """
        global diccionario_clientes
        global diccionario_ejecutivos
        print("**Iniciar sesión en su cuenta**")

        for intento in range(3):  # Tres intentos máximos
            numero_cuenta = int(input("Ingrese su número de cuenta: \n"))
            contrasena = input("Ingrese su contraseña: \n")

            # Verificar existencia del usuario
            if numero_cuenta in diccionario_ejecutivos:
                usuario = diccionario_ejecutivos[numero_cuenta]
                if contrasena == usuario.contrasenia:
                    print(f"-> Iniciando sesión para el ejecutivo {numero_cuenta}...")
                    print("Inicio de sesión exitoso.")
                    # lógica específica para ejecutivo
                    sesion = MenuEjecutivo(usuario)
                    sesion.menu()
                    # Mandarlo a su menú ejecutivo
                    break  # Salir del bucle si el inicio de sesión es exitoso

            elif numero_cuenta in diccionario_clientes:
                usuario = diccionario_clientes[numero_cuenta]
                if contrasena == usuario.contrasenia:
                    print(f"-> Iniciando sesión para el cliente {numero_cuenta}...")
                    print("Inicio de sesión exitoso.")
                    # lógica específica para cliente
                    sesion = MenuCliente(usuario)
                    sesion.menucliente()
                    break  # Salir del bucle si el inicio de sesión es exitoso
            else:
                print("Número de cuenta o contraseña no válidos. Inténtelo de nuevo.")

        else:
            print(
                "Número máximo de intentos alcanzado. Cierre la aplicación e inténtelo de nuevo."
            )

    def registrar_cliente(self):
        """Registra un cliente nuevo
        """
        global df_cliente_global
        global df_ejecutivo_global
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
        df_cliente_global = Banco.registrar_cliente(cliente_nuevo, df_cliente_global)
        Banco.guardar_clientes(df_cliente_global)
        Banco.guardar_ejecutivos(df_ejecutivo_global)
