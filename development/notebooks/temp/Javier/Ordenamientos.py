class QuickSort:
    def __init__(self, array:list):
        self._array=array
    
    @property
    def array(self):
        return self._array 

    def ordenamiento(self):
        if(len(self.array)<=1):
            return self._array
        pivote=self._array[len(self._array)//2]
        izquierda=[x for x in self._array if x<pivote]
        centro=[x for x in self._array if x==pivote]
        derecha=[x for x in self._array if x>pivote]
        self._array.clear()
        self._array=izquierda.copy()
        orden_izq=self.ordenamiento()
        self._array.clear()
        self._array=derecha.copy()
        orden_der=self.ordenamiento()
        return orden_izq + centro + orden_der

class AdminOrdenamientos:
    _arrays_no_ordenados=[]
    _arrays_ordenados=[]
    def __init__(self, array_a_ordenar):
        self._array=array_a_ordenar
    
    @property
    def array(self):
        return self._array
    @array.setter
    def array(self, array_setter):
        self._array=array_setter
        self._arrays_no_ordenados.append(self._array)
    @property
    def arrays_no_ordenados(self):
        return self._arrays_no_ordenados
    @property
    def arrays_ordenados(self):
        return self._arrays_ordenados
    
    def seleccionar_orden(self):
        self._arrays_no_ordenados.append(self._array)
        select="None"
        while True:
            select=str(input("Ingrese el ordenamiento a utilizar (Quicksort o Bubblesort):"))
            if select!="Quicksort" and select!="Bubblesort":
                raise Exception("No coincide con los metodos disponibles.")
            break
        if select=="Quicksort":
            quick_obj=QuickSort(self._array)
            self._arrays_ordenados.append(quick_obj.ordenamiento())
            print("El arreglo ordenado es:",self._arrays_ordenados[-1], sep='\n')
        else:
            bubble_obj=BubbleSort(self._array)
            self._arrays_ordenados.append(bubble_obj.ordenamiento())
            print("El arreglo ordenado es:",self._arrays_ordenados[-1], sep='\n')

class BubbleSort:
    def __init__(self, array):
        self._array=array
    
    @property
    def array(self):
        return self._array
    
    def ordenamiento(self):
        for i in range(len(self._array)-1):
            for j in range(len(self._array)-i-1):
                if self.array[j]>self.array[j+1]:
                    aux=self.array[j]
                    self.array[j]=self.array[j+1]
                    self.array[j+1]=aux
        return self._array

#Flujo
import os
array=[]
admin_obj=AdminOrdenamientos(array)
print("***Programa para ordenar arreglos***")
while True:
    while True:
        elemento=input("Ingrese el valor (Ingrese NO para parar):")
        if elemento=="NO":
            if not len(array)==0:
                break
            else:
                print("El array debe tener elementos.")
        else:
            array.append(int(elemento))
    admin_obj.array=array
    admin_obj.seleccionar_orden()
    eleccion=input("Desea ordenar otro arreglo? (Si/NO):")
    if eleccion=="NO":
        break
    os.system("cls")
print("Adios.")
    