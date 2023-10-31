# [Hector Francisco Badillo Dominguez.](https://github.com/HectorBadillo)
Examen Programacion orientada a objetos.

Biblioteca.

El programa es una gestion de biblioteca y funcionara iniciando sesion de 2 formas: como cliente o como administrador.
## Instrucciones:
## Cliente.
Iniciar Sesion como cliente:
- Necesitaras ingresar Usuario:Hector y Contaseña:Examen 

Funcionalidades:
- Buscar libros.
    - Ejemplo: Seleccionas 1 y se busca el libro: Cien años de soledad.
- Prestar libro.
    - Ejemplo: Una vez buscado el libro se ingresa la opcion para el prestamo.
    - Se presiona 2 para salir de los prestamos.
- Mostrar catalogo de libros.
    - Ejemplo: Selecciona 2 y se muestra la lista de libros.
- Devolver libros.
    - Ejemplo: Selecciona 3 y se escribe: Cien años de soledad.

> El efecto de prestar y devolver libro cambia el status del mismo
> permitiendo que no se preste 2 veces un mismo libro y que no se pueda
> devolver un libro que no haya sido prestado.
---

## Cambiar de Usuario
Para cambiar de usuario cliente a administrador o viseversa:
- Se selecciona la opcion 4 del menu es decir salir.
- Evitas cerrar el programa presionando 2.
- Inicias sesion como el usuario que desees.
---

## Administrador
Iniciar Sesion como cliente:
- Necesitaras ingresar Usuario:Administrador y Contaseña:Examen 

Funcionalidades:
- Mostrar catalogo de libros.
    - Ejemplo: Presiona la opcion 1 y se muestra la lista de libros.
- Añadir libros.
    - Ejemplo: Selecciona la opcion 2, Titulo: Algebra lineal, Autor: Eduardo Solar.
- Eliminar libros.
    - Ejemplo: Selecciona la opcion 3, Titulo: Algebra lineal

> Lo libros que se añaden por defecto tienen status: disponible.

---

> El programa por defecto tendra una pequeña lista de libros para poder observar
> el funcionamiento del mismo, tendra solo un cliente registrado y un administrador registrado
> podras añadir mas libros, eliminarlos, cambiar de usuario administrador a cliente, pedir prestamos y 
> hacer devoluciones todo a traves de los menus.