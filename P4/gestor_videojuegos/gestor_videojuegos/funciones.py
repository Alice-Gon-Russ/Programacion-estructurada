import mysql.connector
#Crear la conexion con la BD

def centrar(texto):
    print(texto.center(80))
    
HOST = "127.0.0.1"
USUARIO = "root"
BASE_DATOS = "gestion_videojuegos_bd4"

def borrarPantalla():
    print("\033c")
    
def esperarTecla():
    input("\n── ⋅ ¡Oprima cualquier tecla para continuar! ⋅ ──")
    
def terminar():
    borrarPantalla()
    input("૮︵⭒‿᧔ !GRACIAS POR UTILIZAR NUESTRO SISTEMA ᧓‿⋆︵౨")
    input("── ⋅\t vuelva pronto! ⋅ ── ")
    
def opcionInvalida():
    input("\n\t── ⋅ ¡Opcion invalidad oprima cualquier tecla para continuar ! ⋅ ──")

def accionNoExitosa():
    input("\n\t── ⋅ ¡Esta accion no pudo realizarse en este momento! ⋅ ──")
    

def accionExitosa():
    input("\n\t── ⋅ ¡Accion Realizada con Exito! ⋅ ──")

def menuPrincipal():
    print("=" * 80)
    centrar("૮︵⭒‿᧔ MENU PRINCIPAL ᧓‿⋆︵౨")
    print("=" * 80)
    opcion=input("\n\t 1.- Menu de videjuegos \n\t 2.- Menu de empresas \n\t 3.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

    
def conectar():
    try:
        conexion=mysql.connector.connect(
        host=HOST,
        user=USUARIO,
        password="",
        database=BASE_DATOS

        )
        return conexion
    except:
        borrarPantalla()
        input("── ⋅ ¡Por el momento no es posible establecer conexion entre el sistema o aplicacion y la base de datos, intente mas tarde!⋅ ──")
        return None
