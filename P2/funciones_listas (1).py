"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

"print(\033c)"

paises=["España","Francia","Italia","Portugal"]

nuemeros=[1,2,3]

varios=["Hola",1,2.5,True]

vaica=[]

#Imprimir el contenido de una lista
print(paises)
print(nuemeros)
print(vaica)
print(varios)
print(paises[3])

#Recorrer la lista 
#1er forma 

for i in paises:
    print(i)
# #2do forma 
for i in range(0,len(paises)):
    print(paises[i])


#ordenar elementos de una lista
paises=["España","Francia","Italia","Portugal"]
print(paises)
paises.sort()  
print(paises)

#dar la vuelta a una lista
paises.reverse()
print(paises)



#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Alemania")
print(paises)

#2da forma
paises.insert(2,"Reino Unido")
print(paises)
paises.insert(8,"Australia")
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma

paises.pop(4)
print(paises)

#2da forma 

paises.remove("Reino Unido")
print(paises)
paises.pop(4)
print(paises)

#Buscar un elemento dentro de la lista
if "España" in paises:
    print("España está en la lista")
else:
    print("España no está en la lista")

#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros=[23,45,8,24,100,0,-1,-10,23,24,8,23,50]
print(numeros)
numeros=int(input("Ingrese el numero a buscar: "))
cuantos=nuemeros.count(numeros)
print("El numero", numeros, "aparece", cuantos, "veces en la lista")

#Conocer la posicion o indice en el que se encuentra un elemento de la lista

posicion=paises.index(100)
print(f"El numero 100 se encuentra en la posicion {posicion} de la lista")

#Unir el contenido de una lista dentro de otra lista
numeros=[23,45,8,24,100,0,-1,-10,23,24,8,23,50]
print(nuemeros)
numeros2=[500,1000]
numeros.extend(numeros2)
print(nuemeros)
#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente

numeros.sort()
numeros.reverse()
print(numeros)