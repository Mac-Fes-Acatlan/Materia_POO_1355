# Biblioteca_Examen_27oct
Hecho por: Flores Gómez Javier Alberto
## Descripción
El siguiente conjunto de códigos fue elaborado con el propósito de simular el sistema que usa una biblioteca para administrar sus libros.
Los archivos:
- administrar_dataframes.py
- biblioteca.py
- libro.py
- menu.py
- usuario.py

Son códigos los cuales poseen enteramente clases y ningún tipo de flujo en ellos.
Mientras que, los archivos:
- main.py
- list_of_books.csv

Poseen el ejecutable del conjunto de códigos y la lista de libros de la biblioteca respectivamente.
## Funcionalidades

- Iniciar sesión con un usuario
- Desplegar la lista de libros y su cantidad
- Actualizar la cantidad de libros en .csv
- Poder pedir prestado libros.
- Poder reservar libros.
- Poder hacer devoluciones de libros.

## Flujo
Inicio de sesión:
> Sólo hay dos posibles usuarios, ambos tienen las mismas funcionalidades.

- En el usuario puede ingresar "Javier" o "Josue" como guste, mientras que para la contraseña, ambos usan la misma "1234A"

Posteriormente, se abrirá el menú de opciones:
- Ingrese "1" para desplegar todos los libros disponibles e información extra.

Se despliegan todos los libros y regresa al menu inicial.
>En este paso puede utilizar el número que guste para acceder a distintas funcionalidades, sin embargo, iremos en orden.

- Ingrese "2" para acceder a la interfaz de préstamo de libros.
- Deberá ingresar el título del libro, sin embargo, ingresaremos "Christine", el cual es un libro que no tiene copias disponibles.
- Después de que nos lo indique el programa, ingresaremos el libro "Cujo", un libro con copias disponibles.
- Se ingresa "1" para hacer el préstamo.

Se imprime el libro pedido y se nos regresa al menu principal.
- Ahora, probaremos con la tercera opción, se ingresa "3".
- Esta interfaz es para reservar libros, se ingresa "Hamlet" un libro con copias disponibles.
- Se ingresa "1".

Se nos indica que el libro fue reservado, ahora bien, si regresamos a la reserva, se podrá pedir el libro.
- Se ingresa "3".
- Se nos indica que tenemos un libro pendiente, ingresamos "1" para pedirlo.

Ahora tenemos 2 libros en posesión, ahora se pedirá otro para comprobar que nuestro máximo de libros es de 3.
- Se ingresa "2".
- Se ingresa el titulo "The War of the Worlds".
- Se ingresa "1".

Se nos presta el libro, si gusta puede verificar que en el .csv se eliminó una copia de los libros que solicitamos. Ahora, se regresará a pedir otro libro para confirmar que no podemos tomar más.
- Se ingresa "2".

Se nos indica que ya no podemos pedir más libros, así que los devolveremos.
- Se ingresa "4".
- Se ingresa "1".
- Se ingresa "747558167", el isbn de Hamlet, libro que tenemos, para poder regresarlo.
- Se ingresa "1".

Se confirma que hemos regresado el libro.
- Ingrese "4".
- Ingrese "2" (para volver al menú).
Como se puede ver, ya sólo tenemos 2 libros en posesión, por lo que ya podemos pedir otro o reservar, sin embargo, saldremos del programa puesto que ya se vieron todas las funcionalidades. Sin embargo, es libre de experimentar con el código todo lo que quiera.
- Ingrese "5".

Finalmente, se sale del programa y termina el test.