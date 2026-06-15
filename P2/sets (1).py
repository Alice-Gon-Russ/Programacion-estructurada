"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")
set1={"Python","SQL","ESTRUCTURADO"}
print(set1)

set2={"Hola",True,33,3.1416}
print(set2)

set2_respaldo=set2.copy()
set2.clear()
print(set2)


set3={""}
print(set3)

set2.add("Hola","Ture","2")
print(set3)
set3.add(10.0)
set3.add(3)
set3.add("3")
print(set3)

set3.pop()
set3.pop()
print(set3)
set3.clear()
print(set3)
set3.add("")

Lista=[10,9,5,8.5,3.4,8.5,10]
print(Lista)
conjunto=set(Lista)
Lista=list(conjunto)
print(Lista)

set1=("Python","SQL","Estructurado",)
#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

lista_correos = []

print("--- Registro de Alumnos UTD ---")
print("Introduce los correos electrónicos de los alumnos.")
print("Escribe 'salir' para terminar el registro.\n")

while True:
    email = input("Ingresa el email del alumno: ").strip().lower()
    
    if email == 'salir':
        break
    if email:
        lista_correos.append(email)
    else:
        print("El correo no puede estar vacío. Intenta de nuevo.")

correos_sin_duplicados = list(set(lista_correos))

print("\n" + "="*30)
print(f"Total de correos ingresados: {len(lista_correos)}")
print(f"Total de correos sin duplicados: {len(correos_sin_duplicados)}")
print("="*30)

print("\nLista de correos únicos:")
for correo in correos_sin_duplicados:
    print(f"- {correo}")

# #Solucion 1
emails = []

resp = "SI"

while resp.upper() == "SI":
    email = input("Email: ").strip()
    emails.append(email.lower())
    resp = input("¿Deseas ingresar otro email (S/N)? ").upper().strip()
emails_set = set(emails)
lista_final = list(emails_set)
print("Lista de emails únicos:", lista_final)

# #Solucion 2
lista_email = []

while True:
    email = input("Ingresa un email: ").lower().strip()
    lista_email.append(email)
    opc = input("¿Deseas ingresar otro email (S/N)? ").upper().strip()
    if opc == 'N':
        break

print("Lista final:", lista_email)

emails_set=set(emails)
lista_emails(set_email)

print(lista_emails)