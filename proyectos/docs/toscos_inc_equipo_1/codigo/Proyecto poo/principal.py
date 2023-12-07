from Login import *

OPC = 0
while OPC != 3:
    print(
        """Menu Inicial
        1. Entrar al sistema
        2. Gestionar Sistema
        3. Salir
            """
    )
    OPC = int(input("Opcion: "))
    if OPC == 1:
        sesion = Login()
        sesion.iniciar_sesion()
    elif OPC == 2:
        print(
            """Menu de CSV
              1. Generar csv de clientes
              2. Generar csv de ejecutivos
              """
        )
        CSV = int(input("Opcion: "))
        if CSV == 1:
            df_cliente_global = Banco.generar_csv_clientes()
        elif CSV == 2:
            df_ejecutivo_global = Banco.generar_csv_ejecutivos()
            df_ejecutivo_global = MenuEjecutivo.registrar_ejecutivo_nuevo(
                df_ejecutivo_global
            )
        df_cliente_global, diccionario_clientes = Banco.lectura_clientes()
        df_ejecutivo_global, diccionario_ejecutivos = Banco.lectura_ejecutivos()
