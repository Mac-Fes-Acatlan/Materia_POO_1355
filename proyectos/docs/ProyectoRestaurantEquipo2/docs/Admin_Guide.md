# Admin_Guide 
**-Simulacion de la terminal-**

```
Bienvenido
¿Desea iniciar sesión o registrarse?
Ingrese 1 si desea iniciar sesión.
Ingrese 2 si desea registrase.
Ingrese 3 si desea salir:
```
-Seleccionando la opción 2: ***Ingrese la opcion 2 si desea registrarse.***  
Se nos deplegará el siguiente menú:

```
Ingrese el número de lo que quiere hacer:
1) Nuevo administrador
2) Salir
```

Para esta guía, seleccionaremos la opción 1: ***"Nuevo Administrador"***

La cual nos desplegará el siguiente formulario el cual llenaremos con los siguientes datos ejemplo:  *AdminArmando32, Armando Casas, ArmandoArmandoCasas123, Av Siempre Viva 742, 5554530739*   

NOTA: "Estos se guardará en un archivo llamado Administradores.csv"
```
Ingrese el usuario del administrador (ingrese 3 para cancelar la operación):
Ingrese el nombre del administrador: 
Ingrese la contraseña del administrador:
Ingrese la dirección del administrador: 
Ingrese teléfono del administrador: 
```

Seguido, se se nos desplegará la informacion previamente ingresada de la siguiente forma: 

```
AdminArmando32
Armando Casas
ArmandoArmandoCasas123
Av Siempre Viva 742
5554530739

Si hay algún dato erroneo, favor de ingresar 1, si todos los datos son correctos ingresar 2:
```
Seleccionando la opción 2, asumiento que ***"todos los datos son correctos"***

Posterior a eso, se nos despliega el siguiente menú de Administrador:
```
¿Qué desea hacer hoy?
Ingrese alguna de las siguientes opciones:
1) Ver los ingredientes.
2) Comprar ingredientes.
3) Salir.
```

Seleccionando la opción 1: ***Ver los ingredientes***  

Se despliega el siguiente Dataframe con todos los ingredientes en el inventario.   
NOTA: **Las columnas _4 y _5 representan los precios de compra y venta de su respectivo articulo**
>Ingredientes:

|   ID | Nombre               | Categoria  | Cantidad |  _4 |  _5 |
|-----:|----------------------|------------|----------|-----:|-----:|
|    1 | Carne molida         | Proteina   |    50.8  |  45 |  150 |
|    2 | Pan de hamburguesa   | Pan        |    19.95 |   5 |   80 |
|    3 | Cebolla              | Verdura    |    10.0  |   3 |   60 |
|    4 | Queso                | Lacteo     |    14.95 |  10 |  160 |
|    5 | Queso cheddar        | Lacteo     |    15.0  |  15 |  200 |
|    6 | Cebolla caramelizada | Condimento |    10.0  |   5 |   80 |
|    7 | Salsa BBQ            | Salsa      |    15.0  |  10 |  100 |
|    8 | Portobello asado     | Seta       |    10.0  |  10 |  140 |
|    9 | Pan integral         | Pan        |    20.0  |   5 |  100 |
|   10 | Queso feta           | Lacteo     |    10.0  |  20 |  500 |
|   11 | Filete de pescado    | Proteina   |    15.0  |  30 |  120 |
|   12 | Pechuga de pollo     | Proteina   |    30.0  |  30 |  120 |
|   13 | Refresco             | Bebida     |   149.5  |  25 |   15 |

```
Ingrese alguna de las siguientes opciones:
1) Ver los ingredientes.
2) Comprar ingredientes.
3) Salir.
```
Seleccionando la opcion 2 ***"Comprar ingredientes"***

Para este ejemplo, usaremos como referencia el ID **1**, el cual representa "Carne Molida" y será el unico ingrediente el cual compraremos.

```
Ingrese el numero del ingrediente a comprar (Ingrese 0 para cancelar):  


Ingrese la cantidad en kg a comprar:  
1  

Ingrese 1 si desea comprar otra cosa, sino ingrese 2:  
2  
```

Al seleccionar la opción 2, nos devolverá al menú de ingredientes inicial, donde podremos volver a elegir en ver nuestro inventario **Actualizado** (con lo previamente comprado) de ingredientes o comprar más:
```
Ingrese alguna de las siguientes opciones:
1) Ver los ingredientes.
2) Comprar ingredientes.
3) Salir.
```

Para demostrar que la lista de ingredientes se ha atualizado con la nueva compra de 1kg de Carne Molida que compramos, seleccionaremos la opcion 2: ***"Ver los ingredientes."***

```
Ingredientes:
```

|   ID | Nombre               | Categoria  | Cantidad |  _4 |  _5 |
|-----:|----------------------|------------|----------|-----:|-----:|
|    1 | Carne molida         | Proteina   | 51.8     |  45 |  150 |
|    2 | Pan de hamburguesa   | Pan        | 19.95    |   5 |   80 |
|    3 | Cebolla              | Verdura    | 10.0     |   3 |   60 |
|    4 | Queso                | Lacteo     | 14.95    |  10 |  160 |
|    5 | Queso cheddar        | Lacteo     | 15.0     |  15 |  200 |
|    6 | Cebolla caramelizada | Condimento | 10.0     |   5 |   80 |
|    7 | Salsa BBQ            | Salsa      | 15.0     |  10 |  100 |
|    8 | Portobello asado     | Seta       | 10.0     |  10 |  140 |
|    9 | Pan integral         | Pan        | 20.0     |   5 |  100 |
|   10 | Queso feta           | Lacteo     | 10.0     |  20 |  500 |
|   11 | Filete de pescado    | Proteina   | 15.0     |  30 |  120 |
|   12 | Pechuga de pollo     | Proteina   | 30.0     |  30 |  120 |
|   13 | Refresco             | Bebida     | 149.5    |  25 |   15 |

```
Ingrese alguna de las siguientes opciones:
1) Ver los ingredientes.
2) Comprar ingredientes.
3) Salir.
```

Seleccionando la opción 3: ***"Salir"***

```
Hasta Luego
```

.