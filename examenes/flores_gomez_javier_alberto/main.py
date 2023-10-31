from biblioteca import Biblioteca
from menu import MenuUsuario

if __name__ == "__main__":
    biblioteca_obj = Biblioteca()
    biblioteca_obj.crear_df()
    menu_obj = MenuUsuario(biblioteca_obj)
    print("\tBienvenido a \"Bukku \" su biblioteca favorita.\nPara continuar, por favor:")
    if menu_obj._menu_inicial(
        menu_obj._validar_usuario()
    )  == 0:
        print("Hasta luego :)")
            