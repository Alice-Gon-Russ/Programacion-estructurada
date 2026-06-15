"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

print("\033c")
#Funciones más comunes en las listas
paises=["Mexico","Canada","EUA","Mexico","Brasil"]
numero=[23,45,8,24]
varios=[33,3.1416,"hola",True]
vacio=[]

#Imprimir el contenido de una lista
print(paises)
print(numero)
print(varios)
print(vacio)
print(paises[0]+" "+paises[3])

#Recorrer la lista 
#1er forma 
for i in paises:
    print(i)

 #2do forma 
for i in range(0,5):
    print(paises[i])

paises=["Mexico","Canada","EUA","Mexico","Brasil"]
print(paises)
#ordenar elementos de una lista
paises.sort()
print(paises)

#dar la vuelta a una lista
paises.reverse()
print(paises)

paises=["Mexico","Canada","EUA","Mexico","Brasil"]
print(paises)
#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Italia")
print(paises)

#2da forma
paises.insert(1,"francia")
print(paises)
paises.insert(100,"Alemania")
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4)
print(paises)

#2da forma 
paises.remove("EUA")
print(paises)

#Buscar un elemento dentro de la lista
busca="Brasil"
if busca in paises:
    print(f"El elemento {busca} está en la lista")
else:
    print(f"El elemento {busca} no está en la lista")

#Contar el numeros de veces que aparece un elemento dentro de una lista



#Conocer la posicion o indice en el que se encuentra un elemento de la lista



#Unir el contenido de una lista dentro de otra lista


#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente




