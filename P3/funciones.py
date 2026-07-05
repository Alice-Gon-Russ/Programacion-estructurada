import mysql.connector

def borrarPantalla():
    print("\033c")
    
def espereTecla():
    input("...¡Oprima cualquier tecla para contunuar!...")
    
def accionExitosa():
    input("...¡Accion Realizada con Exito!...")

def accionNOExitosa():
    input("...¡No fue posible realizar esta Accion intentalo nuevamente!...")   
    
def terminarSistema():
    input("....:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n  vuelve pronto ::::...")
    
def opcionInvalida():
    input("\n\t.... ¡Opcion invalidad, vuelve a intentarlo!.... ")
    
def conectar():
    try:
      conexion=mysql.connector.connect(
         host="127.0.0.1",
         user="root",
         password="",
         database="bd_peliculas_v1" 
      )  
      return conexion 
    except:
       borrarPantalla()
       input("...¡Por el momento no es posible establecer una comunicacion entre el sistema o aplicacion y la base de datos por intentelo mas tarde! ...") 
       return None     
    
