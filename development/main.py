from .administrador_biblioteca import adminBiblio
import pandas as pd

if __name__ == "__main__":
    dict_libro_disponible = {}
    dict_libro_nodisponible = {}
    administrador_obj = adminBiblio(
        dict_libro_disponible, dict_libro_nodisponible
    )
    opc = 0
    while opc != 4:
        while True:
            print("Bienvenido al menu")
            print("1. Agregar libro.")
            print("2. Eliminar libro.")
            print("3. generar colecion.")
            print("4. Salir.")
            opc = int(input("Seleccionar opcion: "))
            if opc in range(1, 5):
                break
            print("Opcion no valida")

        dict_data = administrador_obj.flujo_inventario(opc)
        df_data = pd.DataFrame(dict_data)
        df_data.to_csv("valores_productos.csv", index=False)