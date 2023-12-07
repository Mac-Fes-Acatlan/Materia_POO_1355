"""Codigo que es el ejecutable para el cliente"""
from MenuCliente import MenuCliente
if __name__ == "__main__":
    menu_obj = MenuCliente()
    cliente = menu_obj.inicio_menu()
    if cliente is False:
        print("Adiós.")
    else:
        menu_obj.menu_opciones(cliente)
        print("Hasta luego.")
