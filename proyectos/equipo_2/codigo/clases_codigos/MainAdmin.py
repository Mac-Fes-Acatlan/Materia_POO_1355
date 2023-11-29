"""Codigo que funciona como el ejecutable para el admiistrador"""
from MenuAdmin import MenuAdmin
if __name__ == "__main__":
    menu_admin_obj = MenuAdmin()
    admin = menu_admin_obj.inicio_menu_admin()
    if admin is False:
        print("Adiós.")
    else:
        menu_admin_obj.menu_opciones()
        print("Hasta luego.")
