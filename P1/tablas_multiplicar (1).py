'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones


'''
"""
print("\033c")
numero=int(input("¿que tabla desea multiplicar? "))
multi=numero*1
print(f"{numero} x 1= {multi}")
multi=numero*2
print(f"{numero} x 2= {multi}")
multi=numero*3
print(f"{numero} x 3= {multi}")
multi=numero*4
print(f"{numero} x 4= {multi}")
multi=numero*5
print(f"{numero} x 5= {multi}")
multi=numero*6
print(f"{numero} x 6= {multi}")
multi=numero*7
print(f"{numero} x 7= {multi}")
multi=numero*8
print(f"{numero} x 8= {multi}")
multi=numero*9
print(f"{numero} x 9= {multi}")
multi=numero*10
print(f"{numero} x 10= {multi}")
"""
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control
  2.- Sin funciones


'''
"""
print("\033c")
numero=int(input("¿que tabla desea multiplicar? "))
for num in range(1,11):
    multi=numero*num
    print(f"{numero} x {num}= {multi}")
"""
"""
print("\033c")
numero=int(input("¿que tabla desea multiplicar? "))
num=1
while num<=10:
    multi=numero*num
    print(f"{numero} x {num}= {multi}")
    num+=1
"""
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Con funciones
'''
"""
print("\033c")
def tabla(num_tabla,num):
    multi=num_tabla*num
    print(f"{num_tabla} x {num}= {multi}")
    num+=1 
    return num

num_tabla=int(input("¿que tabla desea multiplicar? "))
num=1

num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)   
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
"""
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control
  2.- Con funciones
'''
print("\033c")
def tabla(num_tabla,num):
    multi=num_tabla*num
    print(f"{num_tabla} x {num}= {multi}")
    num+=1 
    return num

num_tabla=int(input("¿que tabla desea multiplicar? "))
num=1
for i in range(1,11):
    num=tabla(num_tabla,num) 