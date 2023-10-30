from clases.libro import Libro
from clases.biblio import Biblioteca
from clases.autor import Autor
from clases.registro import RegistroInteracciones
from clases.usuario import Usuario

# Un entry point, lo cierto es que nunca me gustó Java, y veo que la POO en general tampoco...

if __name__ == "__main__":

    opcion: int 
    biblio = Biblioteca()
    registro = RegistroInteracciones(biblio)


    print("¡Bienvenido al menú! Vamos a ver cuanto de esto funciona :O")
    while True:
        print("""¿Qué deseas hacer?: 
              1. Crear un libro, 
              2. Crear un usuario,
              3. Añadir un autor con sus obras,
              4. Pedir prestado o devolver un libro,
              5. Ver los registros,
              6. Ver los libros,
              7. Buscar por un método,
              8. Salir del programa""")
        opcion = int(input("Ingresa tu opción: "))
        
        if opcion == 1:
            titulo = input("Ingrese un título: ")
            autor = input("Ingrese un autor: ")
            genero = input("Ingrese un género: ")
            copias_disp = int(input("¿Cuántas copias disponibles hay?: "))
            libro = Libro(titulo, autor, genero, copias_disp)
            biblio.agregar_libro(libro)

        elif opcion == 2:
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = Usuario(nombre)
            biblio.agregar_usuario(usuario)

        elif opcion == 3:
            obras_parametro = []
            nombre = input("Ingrese el nombre del autor: ")
            autor = Autor(nombre)
            num_obras = int(input("¿Cuántas obras desea agregar?: "))
            for i in range(num_obras):

                print(f"Guardando opción {i + 1}: ")
                titulo = input("Ingrese un título: ")
                genero = input("Ingrese un género: ")
                copias_disp = int(input("¿Cuántas copias disponibles hay?: "))
                libro = Libro(titulo, nombre, genero, copias_disp)
                biblio.agregar_libro(libro)
                obras_parametro.append(libro)
            
            autor.agregar_obras(obras_parametro)
            print("Se ha creado el autor y se han añadido sus obras.")        

        elif opcion == 4:
            print("""Seleccione la opción:
                  1. Pedir prestado un libro
                  2. Devolver un libro""")
            
            dev_pres = int(input("Ingrese su opción: "))

            if dev_pres == 1:
                nombre_usuario = input("Es necesario verificar su identidad. Ingrese su nombre: ")
                existe_usuario = registro.verificar_existencia_usuario(nombre_usuario)
                if not existe_usuario:
                    print("El usuario no existe, no se puede prestar el libro.")
                    continue # Volvemos al menú principal
                nombre_libro = input("¿Qué libro desea pedir prestado?: ")
                if not registro.verificar_existencia_libro(nombre_libro):
                    print("El libro no existe, intenta otra vez.")
                registro.prestar_libro(nombre_libro, nombre_usuario)

            elif dev_pres == 2:
                nombre_usuario = input("Es necesario verificar su identidad. Ingrese su nombre: ")
                existe_usuario = registro.verificar_existencia_usuario(nombre_usuario)
                if not existe_usuario:
                    print("El usuario no existe, no se puede devolver el libro.")
                    continue # Misma lógica de arriba.
                nombre_libro = input("¿Qué libro desea devolver?: ")
                registro.devolver_libro(nombre_libro, nombre_usuario)

            else:
                print("Opción no válida, vuelva a intentarlo.")

        elif opcion == 5:
            print("""¿Qué desea hacer?
                  1. Ver los préstamos.
                  2. Ver las devoluciones.""")
            opc = int(input("Seleccione su opción: "))
            
            if opc == 1:
                for usuario, libro in registro._libros_prestados:
                    print(f"{usuario} pidió el libro {libro}")
            elif opc == 2:
                for usuario, libro in registro._libros_devueltos:
                    print(f"{usuario} devolvió el libro {libro}")

            else:
                print("Opción no válida, prueba otra vez.")
        
        elif opcion == 6:
            biblio.__repr__()
        
        elif opcion == 7:
            print("""¿Cómo desea buscar?
                  1. Por género,
                  2. Por autor,
                  3. Por título""")
            opc = int(input("Elija una opción: "))

            if opc == 1:
                genero = input("¿Qué genero quiere buscar?: ")
                biblio.buscar_genero(genero)
            
            elif opc == 2:
                autor = input("¿Qué autor desea buscar?: ")
                mostrar_obras = biblio.buscar_autor(autor)

            elif opc == 3:
                titulo = input("¿Qué libro desea buscar?: ")
                biblio.buscar_libro(titulo)
            
            else:
                print("Opción no válida, vuelve a intentarlo.")

        elif opcion == 8:
            print("Nqvbf, rfcrenzbf dhr ihryinf cebagb :Q") # ROT-13 <tr 'a-mn-zA-MN-Z' 'n-za-mN-ZA-M'>
            break
        
        else:
            print("Opción no válida, prueba otra vez.")
        