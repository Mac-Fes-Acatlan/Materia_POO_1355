#sistema de bibloteca
class Libro:
  def __init__(self, titulo, autor, genero, copias_disponibles):
      self.titulo = titulo
      self.autor = autor
      self.genero = genero
      self.copias_disponibles = copias_disponibles
      self.copias_prestadas = 0

  def restar_unidad(self):
        if self.copias_disponibles > 0:
            self.copias_disponibles -= 1
            self.copias_prestadas += 1

  def sumar_unidad(self):
        if self.copias_prestadas > 0:
            self.copias_disponibles += 1
            self.copias_prestadas -= 1

class Autor:
  def __init__(self):
      self.dict_autor = {
          "Titulos": [],
          "autor": [],
          "Generos": [],
          "Copias Disponibles": [],
          "Copias Prestadas": []
      }

class Usuario:
  def __init__(self, nombre: str):
      self._nombre = nombre
      self.libros_prestados = []

  @property
  def nombre(self):
      return self._nombre

  @nombre.setter
  def nombre(self, nombre_actualizado: str):
      self._nombre = nombre_actualizado

  def tomar_libro(self, titulo_libro, biblioteca):
    for libro in biblioteca.libros:
        if libro.titulo == titulo_libro:
            if libro.copias_disponibles > 0:
                libro.restar_unidad()
                self.libros_prestados.append(libro)
                print(f"El libro '{titulo_libro}' ha sido prestado a {self.nombre}.")
            else:
                print(f"El libro '{titulo_libro}' no está disponible.")
            return  # Importante salir del bucle si el libro se encontró
    print(f"No se encontró el libro '{titulo_libro}'.")


  def devolver_libro(self, titulo_libro, biblioteca):
        for libro in self.libros_prestados:
            if libro.titulo == titulo_libro:
                libro.sumar_unidad()  # Llama a la función sumar_unidad para actualizar las copias disponibles
                biblioteca.registro_interacciones.devolver_libro(titulo_libro, self.nombre)
                self.libros_prestados.remove(libro)
                print(f"El libro '{titulo_libro}' ha sido devuelto por {self.nombre}.")
                return
        print(f"No se encontró el libro '{titulo_libro}' en los libros prestados de {self.nombre}.")




class Biblioteca:
  def __init__(self, autor_instance: Autor):
      self.libros = []
      self.lista_usuarios = []
      self.registro_interacciones = RegistroInteracciones(self)
      self.autor_instance = autor_instance

  def agregar_libro(self, libro):
      # Agregar el libro a la lista de libros en la biblioteca
      self.libros.append(libro)
  
      # Actualizar la información del autor
      self.autor_instance.dict_autor["Titulos"].append(libro.titulo)
      self.autor_instance.dict_autor["autor"].append(libro.autor)
      self.autor_instance.dict_autor["Generos"].append(libro.genero)
      self.autor_instance.dict_autor["Copias Disponibles"].append(libro.copias_disponibles)
      self.autor_instance.dict_autor["Copias Prestadas"].append(libro.copias_prestadas)
  def agregar_usuario(self, usuario):
    self.lista_usuarios.append(usuario)
class RegistroInteracciones:
  def __init__(self, biblioteca):
      self.libros_prestados = []
      self.libros_devueltos = []
      self.biblioteca = biblioteca

  def verificar_existencia_usuario(self, nombre: str):
      for usuario in self.biblioteca.lista_usuarios:
          if usuario.nombre == nombre:
              return True
      return False

  def verificar_existencia_libro(self, titulo: str):
      for libro in self.biblioteca.libros:
          if libro.titulo == titulo:
              return True
      return False

  def prestar_libro(self, titulo_libro: str, nombre_usuario: str):
    if not self.verificar_existencia_usuario(nombre_usuario):
        print(f"No se encontró al usuario '{nombre_usuario}'.")
        return

    if not self.verificar_existencia_libro(titulo_libro):
        print(f"No se encontró el libro '{titulo_libro}'.")
        return

    for libro in self.biblioteca.libros:
        if libro.titulo == titulo_libro:
            usuario = next(u for u in self.biblioteca.lista_usuarios if u.nombre == nombre_usuario)
            if libro.copias_disponibles > 0:
                if libro not in usuario.libros_prestados:
                    usuario.tomar_libro(libro.titulo, self.biblioteca)
                    self.libros_prestados.append((usuario, libro))
                    # Restar una unidad de las copias disponibles
                    libro.restar_unidad()
                    print(f"El libro '{titulo_libro}' ha sido prestado a {nombre_usuario}.")
                else:
                    print(f"'{nombre_usuario}' ya tiene el libro '{titulo_libro}' prestado.")
            else:
                print(f"El libro '{titulo_libro}' no está disponible.")

  def devolver_libro(self, titulo_libro: str, nombre_usuario: str):
      if not self.verificar_existencia_usuario(nombre_usuario):
          print(f"No se encontró al usuario '{nombre_usuario}'.")
          return

      if not self.verificar_existencia_libro(titulo_libro):
          print(f"No se encontró el libro '{titulo_libro}'.")
          return

      for usuario, libro in self.libros_prestados:
          if usuario.nombre == nombre_usuario and libro.titulo == titulo_libro:
              usuario.devolver_libro(titulo_libro, self.biblioteca)
              self.libros_prestados.remove((usuario, libro))
              self.libros_devueltos.append((usuario, libro))
              print(f"El libro '{titulo_libro}' ha sido devuelto por {nombre_usuario}.")

  def mostrar_libros_prestados(self):
      if self.libros_prestados:
          print("Libros prestados:")
          for usuario, libro in self.libros_prestados:
              print(f"{usuario.nombre} tiene prestado el libro '{libro.titulo}'.")
      else:
          print("No hay libros prestados en este momento.")

  def mostrar_libros_devueltos(self):
      if self.libros_devueltos:
          print("Libros devueltos:")
          for usuario, libro in self.libros_devueltos:
              print(f"{usuario.nombre} devolvió el libro '{libro.titulo}'.")
      else:
          print("No hay libros devueltos en este momento.")

class Busqueda:
  def __init__(self, autor_instance: Autor) -> None:
      self.autor_instance = autor_instance

  def listas(self):
      listas = {
          1: "Titulos",
          2: "autor",
          3: "Generos",
      }
      print(listas)
      opcion = int(input("Ingrese opción (1-3): "))
      if opcion in listas:
          campo = listas[opcion]

          if campo == "Titulos":
              titulo_buscado = input("Ingrese el título del libro: ")
              titulos = self.autor_instance.dict_autor["Titulos"]
              if titulo_buscado in titulos:
                  indice = titulos.index(titulo_buscado)
                  autor = self.autor_instance.dict_autor["autor"][indice]
                  genero = self.autor_instance.dict_autor["Generos"][indice]
                  copias_disponibles = self.autor_instance.dict_autor["Copias Disponibles"][indice]
                  
                  print("Información del libro:")
                  print("Título:", titulo_buscado)
                  print("Autor:", autor)
                  print("Género:", genero)
                  print("Copias Disponibles:", copias_disponibles)
                 
              else:
                  print(f"No se encontró información para el título '{titulo_buscado}'.")
          elif campo in self.autor_instance.dict_autor:
              busqueda = input(f"Ingrese {campo}: ")

              if busqueda in self.autor_instance.dict_autor[campo]:
                  resultados = [i for i, valor in enumerate(self.autor_instance.dict_autor[campo]) if valor == busqueda]

                  if resultados:
                      print("Resultados:")
                      for indice in resultados:
                          print(f"-> {self.autor_instance.dict_autor['Titulos'][indice]}")
                  else:
                      print("No se encontraron resultados.")
              else:
                  print(f"No se encontraron resultados para {campo}: {busqueda}")
          else:
              print(f"{campo} no está presente en el registro.")
      else:
          print("Opción no válida")



autor = Autor()
biblioteca = Biblioteca(autor)
busqueda = Busqueda(autor)
registro = RegistroInteracciones(biblioteca)

print("\nBienvenido al sistema de Biblioteca.")
while True:
    print("Por favor, ingrese la opción que desea realizar:")
    print("1. Agregar un libro o usuario")
    print("2. Realizar una búsqueda por título, autor o género")
    print("3. Hacer préstamo o devolución de libro")
    print("4. Mostrar libros prestados o devueltos")
    print("5. Ver el diccionario que muestra todos los libros")
    print("6. Salir del programa")

    opcion = int(input("Ingrese la opción (1-6): "))

    if opcion == 1:
        print("1. Agregar un libro")
        print("2. Agregar un usuario")
        subopcion = int(input("Seleccione una subopción (1-2): "))

        if subopcion == 1:
            # Solicitar información para agregar un libro y agregar el libro a la biblioteca
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            genero = input("Ingrese el género del libro: ")
            copias_disponibles = int(input("Ingrese el número de copias disponibles del libro: "))
            copias_prestadas = int(input("Ingrese el número de copias prestadas del libro: "))


            # Crear una instancia de Libro y agregar el libro a la biblioteca
            libro = Libro(titulo, autor, genero, copias_disponibles)
            biblioteca.agregar_libro(libro)

            print(f"El libro '{titulo}' ha sido agregado a la biblioteca.")

        elif subopcion == 2:
            # Solicitar información para agregar un usuario y agregar el usuario a la biblioteca
            print("Ingrese el nombre del usuario: ")
            nombre_usuario = input()

            # Crear una instancia de Usuario y agregar el usuario a la biblioteca
            usuario = Usuario(nombre_usuario)
            biblioteca.agregar_usuario(usuario)

            print(f"El usuario '{nombre_usuario}' ha sido agregado a la biblioteca.")

    elif opcion == 2:
        # Realizar una búsqueda en la biblioteca
        busqueda.listas()

    elif opcion == 3:
        # Solicitar información de préstamo o devolución
        print("1. Realizar préstamo de libro")
        print("2. Realizar devolución de libro")
        subopcion = int(input("Seleccione una subopción (1-2): "))

        if subopcion == 1:
            # Solicitar información de préstamo
            titulo_libro = input("Ingrese el título del libro a prestar: ")
            nombre_usuario = input("Ingrese el nombre del usuario que realiza el préstamo: ")

            # Comprobar si el usuario y el libro existen y realizar el préstamo
            if not registro.verificar_existencia_usuario(nombre_usuario):
                print(f"No se encontró al usuario '{nombre_usuario}'.")
            elif not registro.verificar_existencia_libro(titulo_libro):
                print(f"No se encontró el libro '{titulo_libro}'.")
            else:
                registro.prestar_libro(titulo_libro, nombre_usuario)

        elif subopcion == 2:
            # Solicitar información de devolución
            titulo_libro = input("Ingrese el título del libro a devolver: ")
            nombre_usuario = input("Ingrese el nombre del usuario que realiza la devolución: ")

            # Comprobar si el usuario y el libro existen y realizar la devolución
            if not registro.verificar_existencia_usuario(nombre_usuario):
                print(f"No se encontró al usuario '{nombre_usuario}'.")
            elif not registro.verificar_existencia_libro(titulo_libro):
                print(f"No se encontró el libro '{titulo_libro}'.")
            else:
                registro.devolver_libro(titulo_libro, nombre_usuario)

    elif opcion == 4:
        print("1. Mostrar libros prestados")
        print("2. Mostrar libros devueltos")
        subopcion = int(input("Seleccione una subopción (1-2): "))

        if subopcion == 1:
            registro.mostrar_libros_prestados()
        elif subopcion == 2:
            registro.mostrar_libros_devueltos()

    elif opcion == 5:
         print(biblioteca.autor_instance.dict_autor)

    elif opcion == 6:
        # Salir del programa
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción válida (1-7).")

print("Gracias por usar la biblioteca.")

