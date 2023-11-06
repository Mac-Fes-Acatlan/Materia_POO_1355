# Sistema Gestor de Biblioteca 

### Programacion Orientada a Objetos 1355

Por: *Jonathan Emanuel Barron Manzano* 
---
---
**-Simulacion de la terminal del sistema-**

```
1. Registrar usuario
2. Registrar libro
3. Registrar prestamo
4. Ver usuarios
5. Ver libros disponibles
6. Ver prestamos 
7. Salir
 
 Elige:
```
*Seleccionando el caso 1* **"Registrar usuario"**

Nos depliega el siguiente menu el cual llenaremos con los siguientes datos ejemplo:
*1, Kenneth Carson, Mojo Dojo Casa House*

```
Ingrese numero de usuario: 1
Ingrese nombre de usuario: Kenneth Carson
Ingrese direccion de usuario: Mojo Dojo Casa House 
```
Seguido de ingresar los datos, se nos mostrará el siguiente mensaje en terminal:

> Usuario registrado exitosamente

Ahora que se ha registrado exitosamente el usuario, procederemos a registrar un libro. 

*Seleccionando el caso 2* **"Registrar libro"**

Se nos desplegará el siguiente menu el cual llenaremos con los siguientes datos ejemplo: 
*01, 1984 Big Brother, George Orwell.true, AA,Ciencia Ficcion.*

```
Ingrese el codigo del libro: 01 
Ingrese el titulo del libro: 1984 Big Brother 
Ingrese el autor del libro: George Orwell
El libro está disponible? [true/false]: true 
Ingrese la localizacion del libro: AA
Ingrese el genero del libro: Ciencia Ficcion
```

Seguido de ingresar el libro con sus respectivos datos, se nos desplegará el siguiente mensaje: 

> Libro registrado correctamente 

Ahora que se ha registrado correctamente un Libro, podemos pasar a la opcion 3 de Registrar un prestamo. 

*Seleccionando caso 3* **"Registrar prestamo"**

Se nos depliega el siguiente menu el cual llenaremos con los datos que previamente usamos para el usuario y codigo de libro: *01,1*

```
Ingrese el codigo del libro: 01
Ingrese el numero de usuario: 1
```
A lo que se nos deplegará el siguiente mensaje: 

>Prestamo registrado exitosamente

Una vez que está registrado el prestamo, podemos hacer uso del 4 para visualizar los usuarios previamente registrados. 

Para este ejemplo, insertaré más ejemplos de usuarios para que se pueda apreciar mejor como se almacenaron en un **DataFrame**. 

*Seleccionando caso 4* **"Ver usuarios"**

numero      |      nombre   |   direccion           |
------------|---------------|-----------------------|
1           |kenneth Carson | Mojo Dojo casa House  |
2           |Jonathan Emanuel| Atizapan 29          |
3           |Cristiano Ronaldo|Calle Siempre Viva 742|


*Seleccionando caso 5* **Ver libros disponibles**

Se nos deplegará el siguiente dataframe, donde el libro que se prestó anteriormente ya no estará disponible. 
Para ejemplificar mejor esta situación, agregué un par de libros ejemplo.

codigo | titulo|   autor       | Localizacion  |genero| disponible  |
-------|----------------|---------------|---------------|------|-------------|
    02 |   IT  |Stephen King| AB|      Terror  |  true              
    03 |Dracula|Bam Stoker  | AC|      Terror  |  true              

*Seleccionando el caso 6* **Ver prestamos**

CodigoLibro |numeroUsuario  |      fecha        |
------------|---------------|-------------------|
1           |1              |2023-10-29 18:53:55|
---
---
Y por ultimo tenemos la opccion 7 para salir del sisteama. 

**NOTA: *Todos los datos igresados se almacenan en 3 archivos CSV, llamados "prestamos", "libros" y "usuarios"***