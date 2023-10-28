from clases.administrador_producto import AdministradorProducto

import pandas as pd

if __name__ == "__main__":

    dict_producto_disponible = {}
    dict_producto_nodisponible = {}
    administrador_obj = AdministradorProducto(
        dict_producto_disponible, dict_producto_nodisponible
    )
    opc = 0
    while opc != 4:
        while True:
            print("Bienvenido al menu")
            print("1. Agregar producto.")
            print("2. Eliminar Producto.")
            print("3. Generar Informe.")
            print("4. Salir.")
            opc = int(input("Seleccionar opcion: "))
            if opc in range(1, 5):
                break
            print("Opcion no valida")

        dict_data = administrador_obj.flujo_inventario(opc)
        df_data = pd.DataFrame(dict_data)
        df_data.to_csv("valores_productos.csv", index=False)
