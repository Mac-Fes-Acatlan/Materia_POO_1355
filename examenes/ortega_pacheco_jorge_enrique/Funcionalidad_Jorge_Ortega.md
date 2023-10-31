# Examen 2° Parcial "Biblioteca"
## Alumno: Ortega Pacheco Jorge Enrique


El código realizado consta de 5 clases que trataran de esbozar un pequeño sistema en el que podamos tener usuarios y un solo administrador, cada uno de ellos con una tarea especifica pero que a la vez alimenta a otras, estas clases son las siguientes:

- class Usuario():  Representa a los usuarios de la biblioteca. Cada usuario tiene su propio conjunto de atributos, incluyendo su nombre, número de cuenta, estado y cantidad de libros prestados.
- class Libro():   Proporciona métodos para buscar libros por título y obtener una lista completa de libros. Los objetos de esta clase contienen información sobre los libros disponibles, como el título, autor, género y copias disponibles.
- class Autores(): Administra un diccionario que almacena nombres de autores y sus respectivas obras. Los administradores pueden agregar autores y sus obras a este diccionario, y los usuarios pueden consultar las obras de un autor específico.
- class Biblioteca(): Es la clase principal que coordina todas las demás clases. Dentro de la clase Biblioteca, se crean instancias de las otras clases. La clase Biblioteca también proporciona un menú de opciones para que los usuarios y los administradores interactúen con el sistema.
- class RegistroInteraccion(): Maneja las operaciones de préstamo y devolución de libros. Los usuarios utilizan esta clase para prestar y devolver libros, y esta clase verifica si hay copias disponibles y si el usuario puede realizar la operación.

## Funcionalidad

Este programa tendra como particularidad el hacer dos menus donde estaran contenidos los metodos y objetos que estaran destinados para cada uno, dentro del menu del usuario tendremos acceso a realizar prestamos, es decir el usuario por si mismo puede hacerse el prestamo del libro si es que tiene una cuenta, en su defecto no lo dejara hacer el prestamo, esto obviamente cae en que tampoco puede hacer devoluciones solo hacer consultas, ya sea por titulo del libro o autor.Por otra parte el administrador tiene la capacidad de agregar obrar y sus respectivos autores, ademas de poder visualizar el catalogo de libros que en nustro caso es una lista de libros. 

## Casos de uso
Es importante mencionar que se han alojado dentro de la inicializacion main un diccionario y una lista de usuarios, cada uno de estos tiene un atributo de instancia, para que usted como usuario pueda hacer la consulta por titulo tendra que colocar forzosamente los títulos de los que se encuentren, en caso de no encontrarse estos el programa arrojara un error diciendo "El libro no se encuentra en la biblioteca.", en su defecto si usted ingresa los que hay le arrojara la informacion de cada uno de ellos que en nuestro caso especifico son: 

- El arte de amar
- Álgebra Lineal
- Leviatán 

Estos libros se encuentran dentro de la clase libros almacenados como un diccionario.

Bien mencionamos que podíamos buscar autores y sus obras, estas obras unicas que se pueden puscar son accedidas por el nombre del autor, que nos devolvera un listado con solo el nombre de los libros y no más datos, estos autores que puede ingresar son: 
- Friedrich Nietzsche
- Herman Hesse
- Simone de Beauvoir
- Platón

Para continuar, como aplicaciones del administrador tendremos la capacidad de agregar autores y obras ademas de poder visualizar lo que tenemos dentro de nustra libreria en cuanto libros, esto es posible a travesl uso de la clase Autores que a su vez tiene inscritos los metodos más precisamente el metodo agregar_autor que nos permite crear un diccionario de listas puesto que primeramente podría ser cualquier cosa al no estar definido pero que en Biblioteca si que esta definido para mandarle listas a la clase.

Es necesario decir que para que el usuario pase de un menu a otro es necesario colocar un 0 cuando se pide ingresar una opcion, esto lo que hace es cerrar el menu del usuario para realizar las actividades del administrador, para salir de ahi es necesario colocar la opcion de salida, en nuestro caso sería la opción 3  que regresara al menu de usuario y posteriormente teclear 5 cuando se pida la indicacion para finalizar el programa.

Los usuarios ya predefinidos y por los cuales se puede revisar con el numero de cuenta son los siguientes: 
- "Jorge", "12345", "Activo", 0
- "Yazmin", "23456", "Activo", 1
- "Leopoldo", "34567", "Activo", 2




