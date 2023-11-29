"""Clase MenuCliente"""
from AdministradorPersonas import AdministradorPersonas
from AdministradorPedidos import AdministradorPedidos
from Menu import Menu
from typing import Union
from datetime import datetime, time
class MenuCliente():
    """Clase que funciona en el main como el menu para el cliente"""
    @staticmethod
    def inicio_menu() -> Union[str,bool]:
        """Metodo que inicia sesion del cliente"""
        admin_personas_obj = AdministradorPersonas()
        print("Bienvenido")
        while True:
            print("¿Desea iniciar sesión o registrarse?")
            print("Ingrese 1 si desea iniciar sesión.",
                "Ingrese 2 si desea registrase.",
                "Ingrese 3 si desea salir: ", sep='\n')
            sesion = int(input(":"))
            if sesion in range(1,4):
                break
            print("Error. Dato incorrecto, pruebe de nuevo.")
        if sesion == 1:
            identificador = admin_personas_obj.inicio_sesion_cliente()
        if sesion == 2:
            identificador = admin_personas_obj.registro_clientes()
        if sesion == 3:
            identificador = False
        if identificador == False:
            print("Hasta Luego.")
        return identificador
    
    @staticmethod
    def menu_opciones(usuario:str)-> int:
        """metodo que muestra todas las opciones a hacer al usuario"""
        admin_personas_obj = AdministradorPersonas()
        admin_pedidos_obj = AdministradorPedidos()
        menu_obj = Menu()
        print("Bienvenido ", usuario,"\n¿Qué desea hacer hoy?")
        while True:
            while True:
                print("Ingrese alguna de las siguientes opciones:",
                    "1) Ver el menú.",
                    "2) Ver pedidos anteriores y recientes.",
                    "3) Ordenar productos.",
                    "4) Salir.", sep = '\n')
                opcion = int(input(":"))
                if opcion in range(1,5):
                    break
                print("Error en el dato, ingrese uno correcto.")
            
            if opcion == 1:
                menu_obj.mostrar_menu()
            elif opcion == 2:
                admin_pedidos_obj.imprimir_pedidos(usuario)
            elif opcion == 3:
                FECHA_INICIO = time(12,0,0)
                FECHA_CIERRE = time(22,0,0)
                fecha = datetime.now()
                if FECHA_INICIO <= fecha.time() <= FECHA_CIERRE :
                    if admin_pedidos_obj.pedir_orden(usuario, menu_obj) == True:
                        print("Su pedido se ha realizado con éxito. Llegará en 30 minutos o menos.")
                else:
                    print("El establecimiento está cerrado, disculpe.")
            else:
                break