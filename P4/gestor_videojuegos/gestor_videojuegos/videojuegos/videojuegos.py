import funciones
from videojuegos import crud
import pandas as pd
from fpdf import FPDF

def menuVideojuegos():
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ MENU DE VIDEOJUEGOS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Vaciar \n\t 7.- Convertir a archivo de texto \n\t 8.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

def agregarVideojuegos(nombre, plataformas, idioma, empresa, conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ AGREGAR VIDEOJUEGOS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    opc="si"
    while opc=="si":
        nombre=input("―୨୧⋆ Nombre del videojuego a agregar: ").upper().strip()
        plataformas=input("―୨୧⋆ Nombre de las plataformas en las que esta disponible: ").upper().strip()
        idioma=input("―୨୧⋆ Idiomas disponibles: ").upper().strip()
        empresa=input("―୨୧⋆ Empresa que desarollo el videjuego: ").upper().strip()
        respuesta=crud.insertar(nombre, plataformas, idioma, empresa, conexionBD)
        if respuesta:
            funciones.accionExitosa()
            opc=input("―୨୧⋆ ¿Deseas agregar otro videjuego (si/no)?: ").lower().strip()
        else:
            funciones.accionNoExitosa()
            respuesta=input("―୨୧⋆ ¿Desea intentar de nuevo (si/no)?: ").lower().strip()
    funciones.esperarTecla()   

def mostrarVideojuegos(conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ MOSTRAR VIDEOJUEGOS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    juegos=crud.consultar(conexionBD)
    if len(juegos)>0:
        lista_videojuegos=[]
    for i in juegos:
        lista_videojuegos.append(i[1])
    if len(juegos)>0:
        print("\n" + "="*80)
        print(f"{'Codigo':<10}{'Empresa':<25}{'Año fundación':<20}{'Pais origen':<20}")
        print("="*80)
        for i in juegos:
            print(f"{i[0]:<10}{i[1]:<25}{i[2]:<20}{i[3]:<20}")

        print("="*80)
    else:
        print("── ⋅ ¡No hay videojuegos que Mostrar, verifique! ⋅ ── ")
    funciones.esperarTecla()
    
def buscarVideojuegos(conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ BUSCAR VIDEOJUEGOS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    nombre=input("―୨୧⋆ Escribe el videojuego a a buscar: ").upper().strip()
    juegos=crud.buscar(nombre,conexionBD)
    if len(juegos)>0:
        print("\n" + "="*80)
        print(f"{'Codigo':<10}{'Empresa':<25}{'Año fundación':<20}{'Pais origen':<20}")
        print("="*80)
        for i in juegos:
            print(f"{i[0]:<10}{i[1]:<25}{i[2]:<20}{i[3]:<20}")
        print("="*80)
    else:
        print("── ⋅ ¡No se encontro el videjuego que estas buscando, verifique! ⋅ ── ")
    funciones.esperarTecla()

def borrarVidejuegos(conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ BORRAR VIDEOJUEGOS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    nombre=input("―୨୧⋆ Escribe el videjuego: ").upper().strip()
    juegos=crud.buscar(nombre,conexionBD)
    if len(juegos)>0:
        print("\n" + "="*80)
        print(f"{'Codigo':<10}{'Empresa':<25}{'Año fundación':<20}{'Pais origen':<20}")
        print("="*80)
        for i in juegos:
            print(f"{i[0]:<10}{i[1]:<25}{i[2]:<20}{i[3]:<20}")
        print("="*80)
        opc=""
        while opc!="si":
         opc=input("―୨୧⋆ ˚¿estas seguro que deseas borrar el videjuego de tu lista (si/no)?").lower().strip()
        if opc=="si":
          respuesta=crud.borrar(nombre,conexionBD)
          if respuesta:
           funciones.accionExitosa()
          else:
           funciones.accionNoExitosa()
    else:
        print("── ⋅ ¡No se encontro el videojuego que estas buscando, verifique! ⋅ ── ")
    funciones.esperarTecla()  
        
def modificarVidejuegos(conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ MODIFICAR VIDEOJUEGOS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    nombre_old=input("―୨୧⋆ Escribe el videojuego a modificar: ").upper().strip()
    juegos=crud.buscar(nombre_old,conexionBD)
    if len(juegos)>0:
        print("\n" + "="*80)
        print(f"{'Codigo':<10}{'Empresa':<25}{'Año fundación':<20}{'Pais origen':<20}")
        print("="*80)
        for i in juegos:
         print (f"{i[0]:<10}{i[1]:<25}{i[2]:<20}{i[3]:<20}")
        opc=""
        while opc!="si":
         opc=input("―୨୧⋆ ˚¿estas seguro que deseas modificar el videojuego (si/no)?").lower().strip()
        if opc=="si":
          nv_nombre=input("―୨୧⋆ ˚Escribe el nuevo nombre del juego: ").upper().strip()
          plataformas=input("―୨୧⋆ ˚Escribe las plataformas en las que esta disponible: ").upper().strip()
          idioma=input("―୨୧⋆ ˚Escribe el idioma en los que esta disponible: ").upper().strip()
          empresa=input("―୨୧⋆ ˚Escribe la empresa que desarollo el juego: ").upper().strip()
          respuesta = crud.modificar(nombre_old,plataformas,idioma,empresa,nv_nombre,conexionBD)
          if respuesta:
           funciones.accionExitosa()
          else:
           funciones.accionNoExitosa()
    else:
        print("── ⋅ ¡No se encontro el videojuego que estas buscando, verifique! ⋅ ── ")
    funciones.esperarTecla()  

def limpiarVideojuegos(conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ BORRAR TODOS LOS VIDEOJUEGOS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    opc=""
    while opc!="si" and opc!="no":
       opc=input("―୨୧⋆ ˚¿estas seguro que deseas borrar TODOS los videojuegos (si/no)?").lower().strip()
    if opc=="si":
        respuesta=crud.vaciar(conexionBD)
        if respuesta:
           funciones.accionExitosa()
        else:
           funciones.accionNoExitosa()
    funciones.esperarTecla()

def obtener_datos_db():
    conexionBD = funciones.conectar() 
    query = "SELECT * FROM videojuegos" 
    df = pd.read_sql_query(query, conexionBD)
    conexionBD.close()
    return df

def exportar_desde_db():
    try:
        funciones.borrarPantalla()
        try:
            df = obtener_datos_db()
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            input("\nPresiona cualquier tecla para regresar...")
            return

        print("==========================================")
        print("  EXPORTAR DATOS DE LA BASE DE DATOS      ")
        print("==========================================")
        print("¿A qué formato deseas exportar la información?")
        print("  1. Texto plano (.txt)")
        print("  2. Excel (.xlsx)")
        print("  3. Documento (.pdf)")

        try:
            opcion = int(input("\nElige una opción: "))
        except ValueError:
            print("\n―୨୧⋆ Opción no válida. Debes ingresar un número.")
            input("\n―୨୧⋆ Presiona cualquier tecla para continuar...")
            return
        nombre_salida = "Videjuguegos_db"
        match opcion:
            case 1:
                funciones.borrarPantalla()
                archivo_txt = f"{nombre_salida}.txt"
                df.to_csv(archivo_txt, sep='\t', index=False) 
                print(f"\n―୨୧⋆ Datos exportados con éxito a: {archivo_txt}")
                
            case 2:
                funciones.borrarPantalla()
                archivo_excel = f"{nombre_salida}.xlsx"
                df.to_excel(archivo_excel, index=False)
                print(f"\n―୨୧⋆ Datos exportados con éxito a: {archivo_excel}")
                
            case 3:
                funciones.borrarPantalla()
                archivo_pdf = f"{nombre_salida}.pdf"
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Times", size=10)
                
                texto_tabla = df.to_string(index=False)
                for linea in texto_tabla.splitlines():
                    linea_limpia = linea.encode('latin-1', 'replace').decode('latin-1')
                    pdf.cell(0, 8, txt=linea_limpia, ln=True)    
                
                pdf.output(archivo_pdf)
                print(f"\n―୨୧⋆ Datos exportados con éxito a: {archivo_pdf}")
                
            case _:
                print("\n―୨୧⋆ Opción no válida.")
        input("\n―୨୧⋆ Presiona cualquier tecla para regresar al menú principal...")

    except Exception:
        funciones.opcionInvalida()
if __name__ == "__main__":
    exportar_desde_db()