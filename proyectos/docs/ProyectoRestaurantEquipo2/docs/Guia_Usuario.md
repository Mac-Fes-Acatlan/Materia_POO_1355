# User_Guide
**-Simulacion de la terminal-**

Una vez iniciado el programa, se nos desplegara el siguiente menú en la terminal:

```
Bienvenido
¿Desea iniciar sesión o registrarse?
Ingrese 1 si desea iniciar sesión.
Ingrese 2 si desea registrase.
Ingrese 3 si desea salir:
```

Seleccionando el caso 2:  **"Ingrese el 2 si desea registrarse"**

Nos despliega el siguiente menú:

```
Ingrese el número de los que quiere hacer:
1) Nuevo Cliente
2) Salir  
```
Seleccionando la opción 1, se nos desplegará el siguiente menú el cual completaremos con los siguientes datos ejemplo:   

**Usuario:** Ale12  
**Nombre:** Alejandro  
**Contraseña:** 12ñ345A  
**Dirección:** Naranjos 3 52679 CDMX  
**Telefono:** 5546753457  
**Correo:** alejandro71234@gmail.com  
**Numero de tarjeta:** 521234567890

NOTA: **Esta informacion se guardare en un DataFrame llamado Clientes.csv**


```
Los datos ingresados fueron: 
Alejandro
Ale12
12ñ345A
Naranjos 3 52679 CMDX
5546753457
521234567890

Si hay algún dato erroneo, favor de ingresar 1, si todos son correctos inrgesar 2

```
Al seleccionar la opcion **1**, se nos mostrará el siguiente menú, en caso contrario podremos regresar a hacer una correccion de los datos que deseamos ingresar.

```
Bienvenido Ale12
¿Qué desea hacer hoy?
Ingrese alguna de las siguientes opciones:
1) Ver el menú.
2) Ver pedidos anteriores y recientes.
3) Ordenar productos.
4) Salir.
```

Seleccionando el caso 1: **Ver el menú**

>El menu es:

| ID | Alimento                | Descripcion                                              | Precio |
|----|-------------------------|----------------------------------------------------------|--------|
| 1  | Hamburguesa Clasica     | Carne molida, Pan de hamburguesa, Queso                   | 78     |
| 2  | Hamburguesa con Queso   | Carne molida, Pan de hamburguesa, Cebolla, Queso cheddar, Queso | 89     |
| 3  | Hamburguesa Vegetariana | Pan integral, Portobello asado, Queso, Queso feta         | 68     |
| 4  | Hamburguesa BBQ         | Carne molida, Pan de hamburguesa, Cebolla caramelizada, Queso cheddar, Salsa BBQ | 82     |
| 5  | Hamburguesa de Pescado  | Filete de pescado, Pan de hamburguesa, Queso              | 59     |
| 6  | Hamburguesa de Pollo    | Pechuga de pollo, Pan de hamburguesa, Queso              | 69     |
| 7  | Hamburguesa de Portobello| Portobello asado, Pan de hamburguesa, Queso cheddar      | 46     |
| 8  | Hamburguesa Gourmet     | Carne molida, Pan integral, Cebolla caramelizada, Queso cheddar, Salsa BBQ | 84     |
| 9  | Agua                    | Agua                                                     | 35     |
| 10 | Refresco                | Refresco                                                 | 25     |

```
Ingrese alguna de las siguientes opciones:
1) Ver el menú.
2) Ver pedidos anteriores y recientes.
3) Ordenar productos.
4) Salir.
```
Seleccionando opcion 3 la cual es: **"Ordenar Productos"**  

El cual nos desplegará de nuevo el menú junto con el siguiente formulario: 

NOTA: ***En este ejemplo el formulario se completará con: 1 ,1 ,1,10 ,1 ,2. Los cuales son valores que corresponden al ID del alimento, cantidad de articulos, opcion a agregar algo más, ID del otro alimento, canidad de articulos del alimento seleccionado y la opcion 2 para cerrar el pedido*** 

>El menu es:

| ID | Alimento                | Descripcion                                              | Precio |
|----|-------------------------|----------------------------------------------------------|--------|
| 1  | Hamburguesa Clasica     | Carne molida, Pan de hamburguesa, Queso                   | 78     |
| 2  | Hamburguesa con Queso   | Carne molida, Pan de hamburguesa, Cebolla, Queso cheddar, Queso | 89     |
| 3  | Hamburguesa Vegetariana | Pan integral, Portobello asado, Queso, Queso feta         | 68     |
| 4  | Hamburguesa BBQ         | Carne molida, Pan de hamburguesa, Cebolla caramelizada, Queso cheddar, Salsa BBQ | 82     |
| 5  | Hamburguesa de Pescado  | Filete de pescado, Pan de hamburguesa, Queso              | 59     |
| 6  | Hamburguesa de Pollo    | Pechuga de pollo, Pan de hamburguesa, Queso              | 69     |
| 7  | Hamburguesa de Portobello| Portobello asado, Pan de hamburguesa, Queso cheddar      | 46     |
| 8  | Hamburguesa Gourmet     | Carne molida, Pan integral, Cebolla caramelizada, Queso cheddar, Salsa BBQ | 84     |
| 9  | Agua                    | Agua                                                     | 35     |
| 10 | Refresco                | Refresco                                                 | 25     |

```
Ingrese el número del producto que desea pedir (Ingrese 0 para cancelar)
: 1
Ingrese la cantidad de articulos que desea: 1
Si desea pedir otra cosa ingrese 1, sino ingrese 2:
: 1 
Ingrese el número del producto que desea pedir (Ingrese 0 para cancelar)
: 10
Ingrese la cantidad de articulos que desea:1
Si desea pedir otra cosa ingrese 1, sino ingrese 2: 2
```
Una vez completado ese formulario, se cierra el pedido y posteriormente se nos despliega el siguiente menú: 

```
Su pedido se ha realizado con éxito. Llegará en 30 minutos o menos.
Ingrese alguna de las siguientes opciones:
1) Ver el menú.
2) Ver pedidos anteriores y recientes.
3) Ordenar productos.
4) Salir.
```
Posterior a esto, elegiremos la opcioón 2 para ver la lista de pedidos, el cual nos lo mostrara en un DataFrame junto con el menú de opciones.


|   | usuario | precio | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | fecha                      |
|---|---------|--------|---|---|---|---|---|---|---|---|---|----|----------------------------|
| 0 | Ale12   | 103.0  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1  | 2023-11-27 13:42:26.751140 |

```
Ingrese alguna de las siguientes opciones:
1) Ver el menú.
2) Ver pedidos anteriores y recientes.
3) Ordenar productos.
4) Salir.
```

Seleccionando la opción 4: ***"Salir"***

```
Hasta Luego 
```