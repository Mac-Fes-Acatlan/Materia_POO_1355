## 2do Examen

### Vilchis Lopez Victor Manuel

Para que el programa compile de la manera mas correcta posible se ofrece este manual a modo de guia para que el ususario sepa que es lo que debe introducir en cada campo

#### 1. Agregar libro

En este campo a manera de inputs se solicitan los datos del libro que se desea agregar.

+ Se solicita el titulo del libro el cual vamos a ingresar
+ Se pide el autor de dicha obra
+ Se ingresa el genero al cual pertenece el libro
+ Se solicita la cantidad de copias disponibles de dicho libro

### 2. Agregar usuario
En esta opcion se crean los diferentes usuarios que podran realizar interacciones dentro de la biblioteca
+ Se solicita el un "ID" para saber si el usuario ya se ha registrado con anterioridad
+ Una vez hecha la confirmacion, se solicita un nombre y edad de dicho usuario
+ Por ultimo, al ser un nuevo usuario los prestamos y devoluciones se inicializan en 0 ya que no se ha prestado ni devuelto nada

### 3. Buscar libro/Prestamos
Esta opcion se le da la posibilidad al usuario de buscar algun libro introduciendo el titulo del mismo.
Posteriormente, se le prgunta si quiere sacar prestado el libro o si no quiere sacarlo
+ Si la opcion es "Si": Se solicita su "ID" para saber si esta registrado, de lo contrario se mostraran que primero debe registrarse. Una vez hecha la verificacion, de forma interna se hace la modificacion a la cantidad de copias disponibles y al numero de prestamos que el usuario ha realizado
+ Si la opcion es "No": Se regresa al menu

### 4. Devolucion
En este apartado, se solicita que ingrese su "ID" y el titulo del libro que esta devolviendo, por lo que de manera interna se modifica la cantidad de copias disponibles de dicho libro, la cantidad de prestamos que tiene el usuario y la cantidad de devoluciones lleva hasta el momento.

### 5. Salir y mostrar interaccion
Por ultimo, en esta opcion se termina las interacciones del usuario con la biblioteca y nos muestra las diferentes interacciones que se realizaron al momento de salirse.
