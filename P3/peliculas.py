import funciones
from peliculas import crud
    
def menuPrincipal():
    print("\t\t....:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion
     
def agregarPeliculas(conexionBD):
    print("\t\t....:::: AGREGAR PELICULAS ::::...\n")
    peli=input("Ingresa la pelicula: ").upper().strip()
    #Insertar en la BD
    respuesta=crud.insertar(peli,conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNOExitosa()
    
def mostrarPeliculas(conexionBD):
    print("\t\t....:::: MOSTRAR PELICULAS ::::...\n")
    print("\tCódigo\t\tPelícula")
    #Consultar en la BD
    pelis=crud.consultar(conexionBD)
    for i in pelis:
        print(f"\t{i}\t\t{i[1]}")
    funciones.espereTecla()
   
def limpiarPeliculas(conexionBD):
     print("\t\t....:::: BORRRAS TODAS PELICULAS ::::...\n") 
     opc=""
     while opc!="si" and opc!="no":
             opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
     if opc=="si":
            respuesta=crud.vaciar(conexionBD)
            if respuesta:
             funciones.accionExitosa()
            else:
                funciones.accionNOExitosa()
            funciones.espereTecla()

    
# def buscarPeliculas(conexionBD):
#     print("\t\t....:::: BUSCAR PELICULAS ::::...\n")   
#     peli=input("Escribe el nombre de la pelicula: ").upper().strip()
#     if peli in pelis:
#         print("\tCódigo\t\tPelícula")
#         for i in range(0,len(pelis)):
#             if peli==pelis[i]:
#               print(f"\t{i+1}\t\t{pelis[i]}")
#         funciones.espereTecla()
#     else:
#         input("\n\t...¡No existe la pelicula que andas buscando!...")

# def borrarPeliculas(conexionBD):
#     posiciones=[]
#     print("\t\t....:::: BORRAR PELICULAS ::::...\n")   
#     peli=input("Escribe el nombre de la pelicula: ").upper().strip()
#     if peli in pelis:
#         for i in range(0,len(pelis)):
#             if peli==pelis[i]:
#               opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
#               while opc!="si" and opc!="no":
#                 opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
#               if opc=="si":
#                 posiciones.append(i)
#         if len(posiciones)>0:
#             for i in range(0,len(posiciones)):
#                 pelis.remove(peli)
#         funciones.accionExitosa()
#     else:
#         input("\n\t...¡No existe la pelicula que andas buscando!...")

# def modificarPeliculas(conexionBD):
#     print("\t\t....:::: MODIFICAR PELICULAS ::::...\n")   
#     peli=input("Escribe el nombre de la pelicula: ").upper().strip()
#     if peli in pelis:
#         for i in range(0,len(pelis)):
#             if peli==pelis[i]:
#               opc=""
#               while opc!="si" and opc!="no":
#                 opc=input("¿Deseas mofificar la pelicula (Si/No)? ").lower().strip()
#               if opc=="si":
#                 pelis[i]=input("Escribe el nuevo nombre: ").upper().strip()
#                 funciones.accionExitosa()
#     else:
#         input("\n\t...¡No existe la pelicula que andas buscando!...")
 


