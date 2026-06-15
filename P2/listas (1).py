from ast import For


print("\033[32m")  # Color verde

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

nuemros=[10,34,56,78,90]
print(nuemros)
lista="["
for i in numeros:
lista+=f"{i} " 
print(lista+"]")

lista="["
for i in range(len(numeros)):
lista+=f"{numeros[i]} "
print(lista+"]")

lista="["
i=0
while i < len(numeros):
lista+=f"{numeros[i]}"
i+=1
print(lista+"]")



#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

#1er forma
Palabras=["UTD","segundo","TI","MTI"]
palabra=input("Ingrese la palabra a buscar: ")
if palabra in Palabras:
    print("La palabra se encuentra en la lista")
else:
  print("La palabra no se encuentra en la lista")

#2DA FORMA
palabras=["UTD","segundo","TI","MTI"]
palabra=input("Ingrese la palabra a buscar: ")
encontro=False
for i in palabras:
if i==palabra:
  encontro=True
if encontro:
 print("La palabra se encuentra en la lista")
else:
 print("La palabra no se encuentra en la lista")
 
#3er FORMA

palabras=["UTD","segundo","TI","MTI"]
palabra=input("Ingrese la palabra a buscar: ")
encontro=False
for i in range(0,len(palabras)):
if palabras[i]==palabra:
  encontro=True
if encontro:
 print("La palabra se encuentra en la lista")
else:
 print("La palabra no se encuentra en la lista")
 
#4ta FORMA

palabras=["UTD","segundo","TI","MTI"]
palabra=input("Ingrese la palabra a buscar: ")
encontro=False
i=0
while i < len(palabras):
if palabras[i]==palabra:
  encontro=True
i+=1
if encontro:
 print("La palabra se encuentra en la lista")
else:
 print("La palabra no se encuentra en la lista")
 
#Ejemplo 3 Añadir elementos a la lista

lista=[","]

#version 1
true=True
while true:
    dato=input("Dame un valor para la lista: ").upper().strip()
    lista.append(dato)
    ture=input("¿Deseas agregar mas elementos a la lista (Si/No)?").lower().strip()
    if true=="no":
        true==False

#  #version 2
true="si"
while true=="si":
    dato=input("Dame un valor para la lista: ").upper().strip()
    lista.append(dato)
    ture=input("¿Deseas agregar mas elementos a la lista (Si/No)?").lower().strip()
print(lista)

lista[0]="Hola"
lista[1]="Oloha"    
  
dato=input("Dame un valor para la lista: ").upper().strip()
lista.append(dato)

print(lista)

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
    ["carlos", "6181234567"],
    ["alberto", "6182344567"],
    ["martin", "6183454567"]
 ]

print(agenda)

for i in agenda:
    print(i)
  
for r in range(0,2):
    for c in range(0,3):
        print(agenda[r][c])

lista=""
for r in range(0,3)
    for c in range(0,2):
        lista+=f"{agenda [r][c]} "
    lista+="\n"
print("["+lista+"]")
