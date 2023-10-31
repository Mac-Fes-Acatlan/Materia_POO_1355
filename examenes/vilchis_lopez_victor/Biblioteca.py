class Usuario:
    def __init__(self, nombre: str, edad: int, id: str, prestamos: int, devoluciones: int):
        self._nombre = nombre
        self._edad = edad
        self._id = id
        self._prestamos = prestamos
        self._devoluciones = devoluciones

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor: int):
        self._edad = valor

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor: str):
        self._id = valor

    @property
    def prestamos(self):
        return self._prestamos
    
    @prestamos.setter
    def prestamos(self, valor: int):
        self._prestamos = valor

    @property
    def devoluciones(self):
        return self._devoluciones
    
    @devoluciones.setter
    def devoluciones(self, valor: int):
        self._devoluciones = valor

class Libro:
    def __init__(self, titulo: str, autor: str, genero: str, copias_disp: int):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._copias_disp = copias_disp

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str):
        self._titulo = valor

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor: str):
        self._autor = valor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor: str):
        self._genero = valor

    @property
    def copias_disp(self):
        return self._copias_disp

    @copias_disp.setter
    def copias_disp(self, valor: int):
        self._copias_disp = valor

class Biblioteca:
    def __init__(self, libros_stock: dict, usuarios_regis: dict):
        self._libros_stock = libros_stock
        self._usuarios_regis = usuarios_regis

    def interaccion(self, opcion: int):
        if opcion == 1:
            titulo = input("\nIngrese el título del libro:").lower()
            autor = input("Ingrese el autor del libro:").lower()
            genero = input("Ingrese el género del libro:")
            cantidad = int(input("Ingrese la cantidad de libros:"))
            libro_obj = Libro(titulo, autor, genero, cantidad)
            self._libros_stock["Titulo"].append(libro_obj.titulo)
            self._libros_stock["Autor"].append(libro_obj.autor)
            self._libros_stock["Genero"].append(libro_obj.genero)
            self._libros_stock["Disponibilidad"].append(libro_obj.copias_disp)
            print("\nEl libro se agregó correctamente")

        if opcion == 2:
            id = input("\nIngrese su ID:")
            if not self._existencia_usuario(id):
                nombre = input("Ingrese el nombre del usuario:")
                edad = int(input("Ingrese la edad del usuario:"))
                prestamos = 0
                devoluciones = 0
                usuario_obj = Usuario(nombre, edad, id, prestamos, devoluciones)
                self._usuarios_regis["Nombre"].append(usuario_obj.nombre)
                self._usuarios_regis["Edad"].append(usuario_obj.edad)
                self._usuarios_regis["ID"].append(usuario_obj.id)
                self._usuarios_regis["Prestamos"].append(usuario_obj.prestamos)
                self._usuarios_regis["Devoluciones"].append(usuario_obj.devoluciones)
                print("\nEl usuario se agregó correctamente")
            else:
                print("El usuario ya existe")

        if opcion == 3:
            buscar_libro = input("\nIngrese el título del libro:").lower()
            if self._buscar_titulo(buscar_libro)!=False:
                opc = input("Sacar libro[S/N]:").lower()
                if opc == "S" or opc == "s":
                    ids = input("Ingresa tu ID:")
                    self._prestar_libro(buscar_libro, ids)
                else:
                    pass

        if opcion == 4:
            devolver_libro = input("\nIngresa el título del libro que vas a devolver:").lower()
            id = input("Ingresa tu ID:")
            self._devolver_libro(devolver_libro, id)

    def _devolver_libro(self, titulo, id):
        if self._existencia_usuario(id):
            if titulo in self._libros_stock["Titulo"]:
                index = self._libros_stock["Titulo"].index(titulo)
                if self._libros_stock["Disponibilidad"][index] > 0:
                    self._libros_stock["Disponibilidad"][index] += 1
                    self._usuarios_regis["Devoluciones"][index] += 1
                    self._usuarios_regis["Prestamos"][index] -= 1
                else:
                    print("No hay libros para devolver de", titulo)
                print("El libro se devolvio con exito , gracias por devolverlo")
            else:
                print("El libro no existe en el inventario")

    def _prestar_libro(self, titulo, ids):
        if self._existencia_usuario(ids):
            if titulo in self._libros_stock["Titulo"]:
                index = self._libros_stock["Titulo"].index(titulo)
                if self._libros_stock["Disponibilidad"][index] > 0:
                    self._libros_stock["Disponibilidad"][index] -= 1
                    self._usuarios_regis["Prestamos"][index] += 1 
                else:
                    print("No hay disponibilidad para el libro", titulo)
            print("Tu prestamo se ha realizado, disfruta el libro")
        else:
            print("Necesitas registrarte")

    def _existencia_usuario(self, id):
        return id in self._usuarios_regis

    def _buscar_titulo(self, libro_busc):
        if libro_busc in self._libros_stock["Titulo"]:
            index = self._libros_stock["Titulo"].index(libro_busc)
            print("Cantidad de libros disponibles:", self._libros_stock["Disponibilidad"][index])
        elif libro_busc in self._libros_stock["Autor"]:
            index=self._libros_stock["Autor"].index(libro_busc)
            print("Obras del autor:",self._libros_stock["Titulo"][index])
            print("Cantidad de libros disponibles:",self._libros_stock["Disponibles"][index])
        else:
            return False

    def _existencia_usuario(self, id):
        if id in self._usuarios_regis["ID"]:
            return True
        else:
            return False

class RegistroInteraccion:
    def __init__(self, lista_interac):
        self._lista_interac = lista_interac

    @property
    def lista_interac(self):
        return self._lista_interac

    @lista_interac.setter
    def lista_interac(self, valores: str):
        self._lista_interac = valores

    def _agregar_interaccion(self, opcion):
        if opcion == 1:
            self._lista_interac.append("Agrego libro")
        if opcion == 2:
            self._lista_interac.append("Agrego usuario")
        if opcion == 3:
            self._lista_interac.append("Busco libro/Prestamos")
        if opcion == 4:
            self._lista_interac.append("Devoluciones")

libros_stock = {
    "Titulo": [],
    "Autor": [],
    "Genero": [],
    "Disponibilidad": []
}

usuarios_regis = {
    "Nombre": [],
    "Edad": [],
    "ID": [],
    "Prestamos": [],
    "Devoluciones": []
}

biblioteca_obj = Biblioteca(libros_stock, usuarios_regis)
listado_interaccion = []
interaccion_obj = RegistroInteraccion(listado_interaccion)
opcion = 0

while opcion != 5:
    while True:
        print("\n")
        print("Bienvenido al menú")
        print("1. Agregar libro")
        print("2. Agregar usuario")
        print("3. Buscar libro/Prestamos")
        print("4. Devoluciones")
        print("5. Salir y mostrar interacciones")
        opcion = int(input("Seleccionar opción: "))
        if opcion in range(1, 6):
            break
        else:
            print("Opción no válida")
    biblioteca_obj.interaccion(opcion)
    interaccion_obj._agregar_interaccion(opcion)

print(listado_interaccion)
print(libros_stock)
print(usuarios_regis)